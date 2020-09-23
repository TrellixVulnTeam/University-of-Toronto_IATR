public class demo {
    public static void main(String[] args) {
        StudentMarkHashMap markus = new StudentMarkHashMap("CSC", 207);
        boolean a = markus.addStudentWithMark("jerry",100);
        markus.addStudentWithMark("subi",99);
        markus.addStudentWithMark("jerry",70);
        System.out.println(markus);
        System.out.println(a);
    }
}
