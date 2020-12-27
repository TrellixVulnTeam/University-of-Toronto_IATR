class GradeEntry:
    '''The base class for a grade entry in a course.
    '''
    def __init__(self,course_ID='',weight=0.0):
        ''' (GradeEntry, str, float) -> NoneType 

        Initializes a grade entry for a given course, given:
        - course_ID: a course identifier, such as 'CSC148'
        - weight: 1.0 credits for a half-course, 2.0 credits for a full course

        This class is not intended to be used for instantiating objects 
        directly, rather an interface (base class).
        '''
        self.course_ID= course_ID;
        self.weight=weight;
        
    def grade_points(self):
        ''' (GradeEntry) -> float

        A grade entry can generate how many points it is worth, based on 
        its grade. The details of how points are generated are left out  
        here and implemented in subclasses.
        '''
        raise NotImplementedError('Subclass needed')


class NumericGradeEntry(GradeEntry):
    '''
    A subclass of GradeEntry that represents a numeric grade entry. 

    Inherits and extends method GradeEntry.__init__()
    Overrides method GradeEntry.grade_points()
    '''
    def __init__(self, course_ID, weight, grade=0.0):
        ''' (NumericGradeEntry, str, float, float) -> NoneType
        Initializes an object representing a numeric grade entry. 

        >>> mygrade = NumericGradeEntry('csc343', 2.0, 85)
        >>> mygrade.grade 
        85
        >>> mygrade.course_ID
        'csc343'
        '''
        GradeEntry.__init__(self, course_ID, weight)
        if(grade>100 or grade<0): #verify the grade is in valid range
            raise Exception('Invalid grade.')
        else:
            self.grade=grade


    def grade_points(self):
        ''' (NumericGradeEntry) -> float 

        This method overrides grade_points() from super class GradeEntry. 
        Returns the point value corresponding to this object's numeric grade. 
        >>> mygrade.grade_points();
        4.0
        '''
        points=-1;
        if(self.grade >= 90): points=4.0
        elif(self.grade >=85): points=4.0
        elif(self.grade >=80): points=3.7
        elif(self.grade >=77): points=3.3
        elif(self.grade >=73): points=3.0
        elif(self.grade >=70): points=2.7
        elif(self.grade >=67): points=2.3
        elif(self.grade >=63): points=2.0
        elif(self.grade >=60): points=1.7
        elif(self.grade >=57): points=1.3
        elif(self.grade >=53): points=1.0
        elif(self.grade >=50): points=0.7
        elif(self.grade >=0): points=0.0
        return points



#global dictionary that maps each letter grade to its point 
#representation according to specs.txt
GRADE_TO_POINTS={'A+':4.0, 'A':4.0,'A-':3.7,'B+':3.3,'B':3.0,'B-':2.7,
                 'C+':2.3, 'C':2.0, 'C-':1.7, 'D+':1.3, 
                 'D':1.0, 'D-':0.7,'F':0.0}

class LetterGradeEntry(GradeEntry):
    '''A subclass of GradeEntry that represents a letter grade entry. 

    Inherits and extends method GradeEntry.__init__()
    Overrides method GradeEntry.grade_points()
    '''
    def __init__(self, course_ID, weight, grade=''):
        ''' (LetterGradeEntry, str, float, str) -> NoneType
        Initializes an object representing a numeric grade entry. 

        >>> mygrade = NumericGradeEntry('csc343', 2.0, 'A')
        >>> mygrade.grade 
        'A'
        >>> mygrade.course_ID
        'csc343'
        '''
        GradeEntry.__init__(self, course_ID, weight)

        if(grade not in GRADE_TO_POINTS): #verify the grade is a valid letter grade
            raise Exception('Invalid grade.')
        else:
            self.grade=grade
        
    def grade_points(self):
        ''' (LetterGradeEntry) -> float 

        This method overrides grade_points() from super class GradeEntry. 
        Returns the point value corresponding to this object's letter grade. 
        >>> mygrade.grade_points();
        4.0
        '''
        return GRADE_TO_POINTS[self.grade];
        