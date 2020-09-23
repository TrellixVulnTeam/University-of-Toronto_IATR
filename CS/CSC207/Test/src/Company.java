

public class Company {
    public Company(){}

    public  void put(String c){
        Manager.add(c);
    }
    public  void pull(String c){Manager.remove(c);}
}
