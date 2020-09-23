import java.io.IOException;
import java.util.HashMap;

public class Demo {
    public static void main(String[] args)throws IOException, ClassNotFoundException {
//        String path = "/Users/jerry/Desktop/serializedobjects.ser";
//
//        Manager m = new Manager(path);
//        Company c = new Company();
//
//         c.pull("one");
//        c.put("one");
//        c.put("two");
//        System.out.println(m.lst.size());

        HashMap hm = new HashMap();
        hm.put("lilei",1);
        System.out.println(hm.get("lilei"));





//        m.saveToFile(path);

//        System.out.println(m.getLst().size());
    }
}
