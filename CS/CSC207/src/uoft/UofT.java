package uoft;

/**
 * Created by pgries on 2017-09-13.
 */
public class UofT {
    public static void main(String[] args) {
        System.out.println("Hello world.");
        String[] paul = new String[] {"Paul", "Gries"};
        String utorid = "g";
        Person p1 = new Person(utorid, paul);
        System.out.println(p1.getId());
        Person p2 = new Person("g", new String[]{"Paul", "Gries"});
        System.out.println(p1 == p2);
        System.out.println(p1.equals(p2));

        //((Object)p1) casting up is never useful
        //Object s = new String("hello"); mislabelling a variable

        System.out.println(p1.toString());

        System.out.println(Student.getNumStudents());
        Student s1 = new Student("a");
        System.out.println(Student.getNumStudents());
        Student s2 = new Student("a");
        System.out.println(Student.getNumStudents());
    }
}
