import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Level;


public class Manager implements Serializable {

    public static HashMap lst;

    public Manager (String filePath) throws ClassNotFoundException, IOException {
        lst = new HashMap();

        File file = new File(filePath);
        if (file.exists()) {
            readFromFile(filePath);
        } else {
            file.createNewFile();
        }
    }

    public void readFromFile(String path) throws ClassNotFoundException {

        try {
            InputStream file = new FileInputStream(path);
            InputStream buffer = new BufferedInputStream(file);
            ObjectInput input = new ObjectInputStream(buffer);

            //deserialize the Map
            lst = (HashMap) input.readObject();
            input.close();
        } catch (IOException ex) {
            System.out.println("can not read ");
        }
    }

    public void saveToFile(String filePath) throws IOException {

        OutputStream file = new FileOutputStream(filePath);
        OutputStream buffer = new BufferedOutputStream(file);
        ObjectOutput output = new ObjectOutputStream(buffer);

        // serialize the Map
        output.writeObject(lst);
        output.close();
    }

    public static void add(String s){
        lst.put(s,1);


    }
    public static void remove(String c){
        lst.remove(c);
    }
//    public ArrayList getLst() {
//        return lst;
//    }
}
