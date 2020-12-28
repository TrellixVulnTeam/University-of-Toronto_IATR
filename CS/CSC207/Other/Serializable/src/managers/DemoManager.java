package managers;

import java.io.IOException;

import university.*;

public class DemoManager {

    public static void main(String[] args)
            throws IOException, ClassNotFoundException {
        demoStudentManager();
    }

    public static void demoStudentManager()
            throws IOException, ClassNotFoundException {

     String csvPath =
             "/Users/jerry/Desktop/serializedobjects.csv";
//      String path =
//              "/Users/lindseyshorser/Documents/Teaching/2016/CSC207/207Lectures2016/w8-2016/managers/serializedobjects.ser";
	String path
                ="/Users/jerry/Desktop/serializedobjects.ser";
        StudentManager sm = new StudentManager(path);
        //System.out.println(sm);

        // Loads data from a CSV for first launch of the program
       // sm.readFromCSVFile(csvPath);
       // System.out.println(sm);

        //Deserializes contents of the SER file
//        sm.readFromFile(path);
        System.out.println(sm);

        // adds a new student to StudentManager sm's records
        sm.add(new Student(new String[] {"Second", "Student"},
                "10102002", "5566778899"));
        sm.add(new Student(new String[] {"First", "Student"},
                "10102001", "1122334455"));
        System.out.println(sm);

        // Writes the existing Student objects to file.
        // This data is serialized and written to file as a sequence of bytes.
        sm.saveToFile(path);
    }
}
