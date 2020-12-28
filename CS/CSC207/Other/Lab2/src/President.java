public class President extends Person{
    private static int counter;

    public President(String firstname, String lastname, String t){
        super(firstname, lastname, t);
        counter += 1;
    }

    @Override
    public String getHonorificName(){
        return "Mister President";
    }

    public String getJobDescription(){
        return "President of the United States" + " " + "#" + counter;
    }
}
