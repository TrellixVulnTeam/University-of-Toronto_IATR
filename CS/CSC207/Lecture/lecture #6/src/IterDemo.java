import java.util.Iterator;

public class IterDemo {
    public static void main(String[] args) {
    AddressBook book = new AddressBook();
    book.add("Yo","213213213","1");
    book.add("Oh","213213213","1");
    book.add("No","213213213","1");

    Iterator<Contact> iter = book.iterator();
    while (iter.hasNext()) {
        System.out.println(iter.next());

        for (Contact c : book){
            System.out.println(c);
        }
    }
    }
}
