import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/** An address book*/
public class AddressBook implements Iterable<Contact> {
    private List<Contact> contacts;

    public AddressBook() {
        contacts = new ArrayList<Contact>();

    }

    public void add(String name, String phone, String email) {
        contacts.add(new Contact(name, phone, email));
    }

    public Iterator<Contact> iterator() {
        return new AddressBookIterator();
    }

    public class AddressBookIterator implements Iterator<Contact> {

        private int nextIndex = 0;


        @Override
        public boolean hasNext() {
            return nextIndex != contacts.size();
        }

        @Override
        public Contact next() {
//            1: remem the next item to return
            Contact c = contacts.get(nextIndex);
//            2: get ready for the next call to next
            nextIndex++;
//            3: return the item I remember
            return c;
//            System.out.println((contacts));
//            return contacts.get(nextIndex++);
        }
    }
}

