
%----------------------------------------------------------------
% class name
\ProvidesClass{csc_assignment}

%----------------------------------------------------------------
% processing options
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions

% load class article
\LoadClass[twoside]{article}

%----------------------------------------------------------------
% packages used
\RequirePackage{fancyhdr}
\RequirePackage{ifthen}
\RequirePackage{amssymb, amsmath}
%\RequirePackage{hyperref}

%----------------------------------------------------------------
%  the counters count the points and output the score table and question count automatically
\newcounter{scorecount}
\setcounter{scorecount}{0}
\newcounter{questioncount}
\setcounter{questioncount}{0}
\newcounter{questioncountpart}
\newcounter{qscorecount}

%----------------------------------------------------------------
% page geometry, header and footer
\setlength{\textwidth}{7in}
\setlength{\textheight}{9.25in}

\setlength{\topmargin}{-0.575in}
\setlength{\oddsidemargin}{-.25in}
\setlength{\evensidemargin}{-.25in}
\setlength{\headheight}{15pt}
\linespread{1.25}

\pagestyle{fancy}
\lhead[]{}
\chead[]{}
\rhead[]{}
\lfoot[]{}
\cfoot[]{}
\rfoot[]{} 
%\rfoot[Page \thepage/\pageref{page:last}]{Page \thepage/\pageref{page:last}}
\fancyfoot[RO,LE]{{Page \thepage}}
\fancyfoot[CO,CE]{{}} %{\studentnumberboxes}
\fancyhead[L]{{
  \ifthenelse{\value{page}=\pageref{page:first}}{}{
    \tiny
    \@InstitutionName
  }
}}

\fancyhead[C]{{
  \ifthenelse{\value{page}=\pageref{page:first}}{}{
    \tiny
    \@CourseCode\@CourseSemesterCode\@CourseSection
  }
}}

\fancyhead[R]{{
  \ifthenelse{\value{page}=\pageref{page:first}}{}{
    \tiny
    \@Date
  }
}}

%----------------------------------------------------------------
% exam info setup commands

\newcommand{\InstitutionName}[1]{\def\@InstitutionName{{#1}}}
\newcommand{\FacultyName}[1]{\def\@FacultyName{{#1}}}
\newcommand{\DepartmentName}[1]{\def\@DepartmentName{{#1}}}

\newcommand{\CourseTitle}[1]{\def\@CourseTitle{{#1}}}
\newcommand{\CourseCode}[1]{\def\@CourseCode{{#1}}}
\newcommand{\CourseSemester}[1]{\def\@CourseSemester{{#1}}}
\newcommand{\CourseSemesterCode}[1]{\def\@CourseSemesterCode{{#1}}}
\newcommand{\CourseSection}[1]{\def\@CourseSection{{#1}}}
\newcommand{\CourseInstructor}[1]{\def\@CourseInstructor{{#1}}}

\newcommand{\Date}[1]{\def\@Date{{#1}}}

\newcommand{\Title}[1]{\def\@Title{{#1}}}

%\newcommand{\}[1]{\def\@{{#1}}}

\newcommand{\AssignmentName}[1]{\def\@AssignmentName{{#1}}}

\newcommand{\StudentName}[1]{\def\@StudentName{{#1}}}

\newcommand{\StudentNumber}[1]{\def\@StudentNumber{{#1}}}

\newcommand{\scoretable}[1]{
\def\@tscoretable{{
}}
\let\@scoretable=\@tscoretable
}

\def\tand{&}
\newcounter{iquestion}
\scoretable{%
  \setcounter{iquestion}{1}%
  \whiledo{\theiquestion<\thequestioncount}{%
    {\theiquestion} \tand  \\%
  \stepcounter{iquestion}%
  }%
    {\theiquestion} \tand ~ \\
}

\newcommand{\QuestionCount}[1]{\setcounter{questioncount}{#1}}
%----------------------------------------------------------------
% set the default values for the course info

\InstitutionName{UNIVERSITY OF TORONTO}
\FacultyName{Faculty of Arts and Science}
\DepartmentName{Department of Computer Science}

\CourseTitle{Course Title}
\CourseCode{Course Code}
\CourseSemester{Course Semester}
\CourseSemesterCode{Course Semester Code}
\CourseSection{Course Section}
\CourseInstructor{Course Instructor}

\Date{Date} %{May 2017}
\Title{Title}

\AssignmentName{Assignment Name}
\StudentName{Your Name}
\StudentNumber{Your Student Number}


%----------------------------------------------------------------
\newcommand{\toppage}{{%
\AssignmentTopPage
}}

%----------------------------------------------------------------
\newcommand{\AssignmentTopPage}{{
\label{page:first}%

\newpage

\begin{center}{{\@CourseCode} {\@CourseSemester} {\@Date} Assignment {\@AssignmentName}}
\end{center}

\begin{tabular}{ll}
{\bf Name:} & \@StudentName \\
{\bf SN:} & \@StudentNumber \\
\end{tabular}

\@scoretable

\vspace{1cm}
%\begin{tabular}{|l|l|}
%\hline
%Question & Score \\
%\hline
%1 & \\
%2 & \\
%3 & \\
%\hline
%Total & \\
%\hline
%\end{tabular}\\
%\par
}}

%----------------------------------------------------------------
% this pages is the last page of the test
% you can edit (e.g. to leave the last page blank)
\newcommand{\bottompage}{{%
\label{page:last}%
}}


%----------------------------------------------------------------
% change the enddocument command to write the information about the
% test to the AUX file

% make a copy of the original enddocument
\let\origenddocument=\enddocument

% define the new version of enddocument
\def\enddocument{
% call the original enddocument at the end to finish the document
  \origenddocument%
}



%----------------------------------------------------------------
% change the begindocument command 

% make a copy of the original enddocument
\let\origdocument=\document

% define the new version of enddocument
\def\document{
% call the original begindocument at the start
  \origdocument%
% the top and marking pages
  \toppage%
}

%----------------------------------------------------------------
\newcommand{\Acknowledgements}[1]{
{\bf Acknowledgements:}\\
{#1}~\\

Name: {\@StudentName} \hfill Date: \today\\
}

%----------------------------------------------------------------
% customization for a course
\InstitutionName{UNIVERSITY OF TORONTO}
\FacultyName{Faculty of Arts and Science}
\DepartmentName{Department of Computer Science}

\CourseTitle{Data Structures and Analysis}
\CourseCode{CSC263}
\CourseSemester{Fall}
\CourseSemesterCode{}
\CourseSection{}

\Date{2017}


\endinput
%%
%% End of file `assignment.cls'.
