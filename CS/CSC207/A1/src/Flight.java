
import java.util.ArrayList;

public class Flight {
	private String name;
	private ArrayList airports;
	private String date;

	public Flight(String name, String date) {
		this.name = name;
		this.airports = new ArrayList();
		this.date = date;
	}

	public void addAirport(Airport a){
	    a.addFlight(this);

	}


	public boolean equals(Flight f){
		return name.equals(f.name)  && date.equals(f.date);
	}

	public ArrayList getAirports(){

		return airports;

	}

	public String getName(){
		return name;

	}

	public String getDate(){
		return date;

	}

	public  String toString(){
	    if (airports.size() == 0){
	        return name + ", " + date;
	    }else if (airports.size() == 1){
	        Airport a = (Airport)airports.get(0);
	        return name + ", " + date + "\n"  + a.getName();
        } else {
	        String res = name  + ", " + date + "\n";
	        int i = 0;
	        while(i != airports.size()-1){
	            Airport a = (Airport) airports.get(i);
	            res = res + a.getName() + "\n";
                i += 1;
            }
            Airport temp = (Airport) airports.get(airports.size()-1);
            return res + temp.getName();
        }
	}

}
