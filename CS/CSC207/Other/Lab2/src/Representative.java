public class Representative extends Person {

    public Representative(String firstname, String lastname, String t){
        super(firstname, lastname, t);
    }

    @Override
    public String getHonorificName(){
        return "The Right Honourable" + firstName + lastName;
    }
}
