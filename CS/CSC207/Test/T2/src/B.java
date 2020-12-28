public class B extends A {
    int j;
    int i;
    private String email;

    public B(String email){
        super(email);
        this.email = "B's email";
    }
    public void m(int i){
        this.i = 3;
    }
}
