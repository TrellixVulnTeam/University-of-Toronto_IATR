
/** A person at the UofT with a name and a UTORid. */
public class Person {

    /** The person's name, with the last name last. */
    String[] name;

    /** This person's UTORid. */
    String id;

    String qq = "359137154";
    /** TODO: write this. */
    public Person(String id, String[] n) {
        this.id = id;
        this.name = n;
    }
}