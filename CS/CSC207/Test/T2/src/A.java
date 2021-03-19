public class A {
    private  String email;
    public A(String email){
        this.email = "A's email";
    }
    static int i = 10;

    @Override
    public String toString() {
        return "this is message of email";
    }

    //    static int f(C c){
//        return i  +c.i;
//    }
}
