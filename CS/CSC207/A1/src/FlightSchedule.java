import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;

public class FlightSchedule {



	public static void main(String[] args) throws IOException {
		ArrayList airports_pool = new ArrayList();

		String fileName = "FlightList.txt";
		Path path = Paths.get(fileName);
		try (BufferedReader fileInput = Files.newBufferedReader(path)) {
			String line = fileInput.readLine();

			while (line != null) { // Reading from a file will produce null at the end.

				String name = line.substring(0, 5);
				String date = line.substring(6,16);

				Flight f = new Flight(name,date);

				int num = (line.length() - 18)/6 ;
				int i = 0;
				while (i != num){
					String ap_name = line.substring(18+i*6, 23+i*6).trim();

					boolean status = false;

					int j = 0;

					while ( j != airports_pool.size()){
						Airport a = (Airport)airports_pool.get(j);
						if (a.getName().equals(ap_name)){
							status = true;
							a.addFlight(f);
						}
					j++;
					}
					if (!status){
						Airport new_a = new Airport(ap_name);
						new_a.addFlight(f);
						airports_pool.add(new_a);

					}
					i++;
				}
				line = fileInput.readLine();
			}
			fileInput.close();
		}




		BufferedReader kbd = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter the name of an airport: ");
		String input = kbd.readLine();

		while (!input.equals("exit")) { // Don't use != because compares memory addresses.


			boolean status = false;
			int counter = 0;

			for (int i = 0; i != airports_pool.size(); i++){
				Airport x = (Airport) airports_pool.get(i);
				if(input.equals(x.getName())){
					status = true;
					counter = i;
				}


			}

			if (!status){
				System.out.println("This is not a valid airport");

			}else{
				Airport y = (Airport) airports_pool.get(counter);
				String res = y.toString();
				System.out.println(res);
			}
			System.out.println("Enter the name of an airport: ");
			input = kbd.readLine();
		}
		kbd.close();
	}
}
