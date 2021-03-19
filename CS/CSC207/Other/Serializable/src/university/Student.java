package university;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Map;

public class Student extends Person implements IDed<String>, Serializable {
    
    	private String studentNum;
	private static int studentCount;
	private Map<String, Grade> courseToGrade;

	public Student(String[] name, String dob, String studentNum) {
		super(name, dob);
		this.studentNum = studentNum;
		studentCount += 1;
		this.courseToGrade = new HashMap<String, Grade>();
	}
	
	// This method records a Grade.
	// It is capable of taking any subclass of Grade, including a
	// LetterGrade, a NumericGrade, or even some future subclass we
	// might define, such as CreditNoCreditGrade.
	public void addGrade(String course, Grade g) {
	    this.courseToGrade.put(course, g);
	}
	
	public void addGrade(String course, int g) throws InvalidGradeException {
	    // Whenever we construct a NumericGrade, an InvalidGradeException
	    // could be thrown.  Because InvalidGradeException extends Exception
	    // and not RuntimeException, it is a "checked" exception.  Therefore,
	    // We must either catch it, or declare that we throw it.
	    this.courseToGrade.put(course, new NumericGrade(g));
	}
	
	//This method will not throw an exception.
	public void addGrade(String course, String g) {
	    this.courseToGrade.put(course, new LetterGrade(g));
	}
	
	// Any time we have more than one method with the same name,
	// we say that that method is "overloaded".  Even though they
	// have the same name, Java can tell the methods apart, because
	// they have different signatures.
	
	// You have seen overloaded methods before, when we saw multiple
	// constructors in a single class.
	
	// Overloaded is different from the concept of overridden!  To help
	// remember which is which, think of the expression in English:
	// "That's a loaded question", which implies that the question 
	// is loaded with meaning.  In Java, a loaded method is a
	// method name that is loaded with meaning: it could mean
	// one method body, or it could mean another.
	
	// For more on overloading, see:
	// https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html
	
	public static int getStudentCount() {
		return studentCount;
	}

	public String getStudentNum() {
		return studentNum;
	}

	@Override
	public String toString() {
		return super.toString() + " , " + this.studentNum;
	}

	public String getID() {
	    return this.studentNum;
	}
}
