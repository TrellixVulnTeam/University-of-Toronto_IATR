/** A person at the UofT with a name and a UTORid. */
public class Person {

    /** The person's name, with the last name last. */
    static String[] name = {"zhangjiayi"};

    /** This person's UTORid. */
    String id;

    /** TODO: write this. */
    public Person(String id, String[] n) {
        this.id = id;
        //this.name = n;
    }
    public static void f(){
       System.out.println("a");
    }

    public static void main(String[] args){
        Person a = new Person("1", new String[] {"2"});
        //a.f();
        System.out.print(a.name);
    }
}

