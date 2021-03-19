
import java.util.ArrayList;

public class Airport {
	private String name;
	private ArrayList flights;

	public Airport(String name) {
		this.name = name;
		this.flights = new ArrayList();
	}

	public String getName() {
		return name;
	}

	public boolean wasVisitedBy(Flight f) {
		boolean res = false;
		int i = 0;
		while (i != f.getAirports().size()) {
			if (f.getAirports().get(i).equals(this)) {
				res = true;
			}
			i += 1;
		}
		return res;
	}

	public boolean onSameFlight(Airport compared_airport) {
		boolean res = false;
		int i = 0;
		while (i != this.flights.size()) {
			int j = 0;
			while (j != compared_airport.flights.size()) {
				if (this.flights.get(i) == compared_airport.flights.get(j)) {
					res = true;
				}
				j += 1;
			}
			i += 1;
		}


		return res;
	}

	public void addFlight(Flight f) {

		flights.add(f);
		f.getAirports().add(this);

	}

	public boolean equals(Airport compared_airport) {
		boolean res = true;
		int i = 0;
		while (i != flights.size()) {
			if (!compared_airport.flights.contains(flights.get(i))) {
				res = false;
			}
			i += 1;
		}
		return this.name.equals(compared_airport.name) && res && flights.size() == compared_airport.flights.size();
	}

	public String toString() {
		String res = "";
		int i = 0;
		if (flights.size() == 0) {
			return name + " " + "()";
		} else {
		while (i != flights.size() - 1) {
			Flight f = (Flight) flights.get(i);
			res = res + f.getName() + ", ";
			i += 1;
		}
		Flight f_2 = (Flight)flights.get(flights.size()-1);
		String temp = f_2.getName();
		return name +" "+ "(" + res + temp +  ")";
	}
	}

}
