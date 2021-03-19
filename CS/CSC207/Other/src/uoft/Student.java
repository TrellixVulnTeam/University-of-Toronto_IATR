package uoft;

/**
 * Created by lindseyshorser on 2017-09-15.
 */
public class Student extends Person{
    private int numCourses;
    private static int numStudents;

    public Student(String id){
        super(id);
        numStudents++;
    }

    public String toString(){
        return super.toString();
    }

    public static int getNumStudents(){
        return numStudents;
    }
}
