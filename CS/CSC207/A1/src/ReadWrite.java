import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class ReadWrite {

    public static void main(String[] args) throws IOException {
	// You could use Scanner instead if you like.
        BufferedReader kbd = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter something: ");
        String input = kbd.readLine();
        while (!input.equals("exit")) { // Don't use != because compares memory addresses.
            System.out.println("You typed " + input);
            input = kbd.readLine();
        }

        System.out.println("Enter a file name: ");
        String fileName = kbd.readLine();
        Path path = Paths.get(fileName);
        try (BufferedReader fileInput = Files.newBufferedReader(path)) {
            String line = fileInput.readLine();
            while (line != null) { // Reading from a file will produce null at the end.
                System.out.println(line);
                line = fileInput.readLine();
            }
        }
    }
}
