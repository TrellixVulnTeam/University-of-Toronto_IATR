/** Manage people at the UofT */
public class UofT {

    // There are no functions. Only methods.

    /**
     * The main method.
     * @param args the command-line arguments.
     */
    public static void main(String[] args) {
        System.out.println("Hello world");
        String id = "g";
        //id = "a";
        System.out.println(id);
        String[] myName = new String[] {"Paul", "Gries"};
        Person p = new Person(id, myName);

        
    }
}

//PCRS
class ImmutablePen {
    private String color;

    public ImmutablePen(String c) {
        this.color = c;
    }

    public String getColor() {
        return color;
    }
}

//public class MutablePen implements Cloneable{
//    private String color;
//
//    public MutablePen(String c) {
//        this.color = c;}
//
//    public String getColor() {return this.color;}
//
//    public void setColor(String newcolor) {color = newcolor;}
//
//    public MutablePen clone() {
//        return new MutablePen (color);
//    }
}