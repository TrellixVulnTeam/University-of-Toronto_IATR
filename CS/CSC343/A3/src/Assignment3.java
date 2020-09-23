import java.sql.*;
import java.util.List;
import java.util.ArrayList;
import java.lang.System;


public class Assignment3 extends JDBCSubmission {

    public Assignment3() throws ClassNotFoundException {
        Class.forName("org.postgresql.Driver");
    }

    /**
     * Connect to a database with the supplied credentials.
     * @param  url       the url for the database
     * @param  username  the username to connect to the database
     * @param  password  the password to connect to the database
     * @return return ture iff connect successfully otherwise false
     */
    @Override
    public boolean connectDB(String url, String username, String password) {
	    //write your code here.


        try {

            //Make the connection to the database, ****** but replace "username" with your username ******
            connection = DriverManager.getConnection(url, username, password);

        } catch (SQLException e) {

            System.out.println("Connection Failed! Check output console");
            e.printStackTrace();
            return false;

        }

        return true;
    }

    /**
     * Disconnect from the database.
     * @return return ture iff disconnect successfully otherwise false
     */
    @Override
    public boolean disconnectDB() {
	    //write your code here.
        try {
        connection.close();
        } catch (SQLException e) {

            System.out.println("Disconnection Failed! Check output console");
            e.printStackTrace();
            return false;
        }
        return true;
    }

    /**
     * Returns the list of Presidents in given country, in descending order of date of occupying the office,
     * and the name of the party to which the president belonged.
     * @param  countryName   name of the country
     * @return Return the ElectionResult which contain the list of Presidents in given country, in descending order of date of occupying the office,
     * and the name of the party to which the president belonged.
     */
    @Override
    public ElectionResult presidentSequence(String countryName)  {
            //Write your code here.
        List<Integer> presidents = new ArrayList<Integer>();
        List<String> parties = new ArrayList<String>();


        try {
            PreparedStatement ps = connection.prepareStatement("SELECT p2.id, p1.name " +
                    "FROM party p1, politician_president p2, country c " +
                    "WHERE c.name = ? and c.id = p2.country_id and p1.id = p2.party_id " +
                    "order by p2.start_date DESC");
            ps.setString(1, countryName);
            ResultSet rs = ps.executeQuery();

            while (rs.next()) {
                int president = rs.getInt(1);

                String party = rs.getString(2);

                presidents.add(president);
                parties.add(party);
            }

            ps.close();
            rs.close();


        } catch (SQLException e) {
            e.printStackTrace();
        }
        return new ElectionResult(presidents, parties);
	}

    /**
     * Given a party, returns other parties that have similar descriptions in the database.
     * @param  partyId          id of the party
     * @param  threshold        Jaccard similarity threshold
     * @return  Return a list of parties that have similar descriptions in the database.
     */
    @Override
    public List<Integer> findSimilarParties(Integer partyId, Float threshold) {
	//Write your code here.

        List<Integer> res = new ArrayList<Integer>();

        String description1 ="";


        try {
            PreparedStatement ps1 = connection.prepareStatement("SELECT description FROM party WHERE id = ?");
            ps1.setInt(1, partyId);
            ResultSet rs1 = ps1.executeQuery();

            while (rs1.next()) {
                description1 = rs1.getString(1);
            }
            ps1.close();
            rs1.close();


            PreparedStatement ps2 = connection.prepareStatement("SELECT id, description FROM party WHERE id <> ?");
            ps2.setInt(1, partyId);
            ResultSet rs2 = ps2.executeQuery();


            while (rs2.next()) {
                int other_id = rs2.getInt(1);

                String description2 = rs2.getString(2);
                double temp;

                temp = similarity(description1, description2);

                if (temp >= threshold){
                    res.add(other_id);
                }
            }
            ps2.close();
            rs2.close();


        } catch (SQLException e) {
            e.printStackTrace();
        }
        return res;
    }

    public static void main(String[] args) throws Exception {
   	    //Write code here. 
	    System.out.println("Hellow World");
    }

}



