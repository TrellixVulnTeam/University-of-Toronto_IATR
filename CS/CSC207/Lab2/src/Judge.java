public class Judge extends Person {
    public Judge(String firstname, String lastname, String t){
        super(firstname, lastname, t);
    }

    @Override
    public String getHonorificName(){
        return "The Honourable" + firstName + lastName;
    }
}
