package uoft;

/**
 * A person at the UofT with a name and a UTORid.
 * Created by pgries on 2017-09-13.
 */
public class Person {

    /** This person's UTORid. */
    private String id;
    /** This person's name. The last name is last. */
    private String[] name;

    /**
     * A new Person named name with UTORid id.
     * @param id the UTORid
     * @param name the name
     */
    public Person(String id, String[] name) {
        this.id = id;
        this.name = name;
    }

    public Person(String id) {
        super();
        this.id = id;
    }

    public Person(){
    }

    public String getId() {
        return id;
    }

    public String[] getName(){
        return name;
    }

    public void setName(String[] name){
        this.name = name;
    }

    public boolean equals(Object obj){
        return obj instanceof Person && this.id == ((Person)obj).id;

    }

    public String toString(){
        return name[1] + ", " + name[0] + "\n" + id;
    }

    //public int hashCode(){
    //    return Objects.hashCode(this.id);
    //}
}
