public class Person {
    String firstName;
    String lastName;
    String title;

    public Person(String firstname, String lastname, String t) {
        this.firstName = firstname;
        this.lastName = lastname;
        this.title = t;
    }
    public String getHonorificName(){
        return this.title + " " +  firstName + " " + lastName;
        }

    public String getName(){
        return firstName + " " + lastName;
    }

    public static void main(String[] args) {
        Person p  = new Person("Paul","Gries","Mr.");
        Representative r = new Representative("Paul","Gries","Mr.");
        Judge j = new Judge("Jerry", "Sun", "Mr.");
        President q_1 = new President("Harry","Li","Mr.");
        System.out.println(q_1.getJobDescription());
        President q_2 = new President("pi","sda","Mr.");
        System.out.println(p.getHonorificName());
        System.out.println(r.getHonorificName());
        System.out.println(j.getHonorificName());

        System.out.println(q_2.getJobDescription());

    }
    }
