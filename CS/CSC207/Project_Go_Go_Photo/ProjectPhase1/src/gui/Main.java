package gui;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import model.GoGoPhotoSystem;


/**
 * Main is the entrance that we create and open our program. It initialize a new program, create a
 * new GoGoPhotoSystem associated with it. Read from the ser file when getting initialized and save
 * the information into the ser file when closing the program.
 * @see GoGoPhotoSystem
 * @see Parent
 * @see Stage
 */
public class Main extends Application {

    public static GoGoPhotoSystem system;
    /**
     * This method launches the whole program.
     * @param args the parameter to get started
     * history text file when the file exists. Otherwise it returns an empty ArrayList.
     */
    public static void main(String[] args) {
        launch(args);
    }

    /**
     * This method is called when the program gets started. Initialize a new GoGoPhotoSystem and set the initial
     * coefficients for the primary scene.
     * @param primaryStage the primary stage to display everything
     * @throws Exception
     */

    @Override
    public void start(Stage primaryStage) throws Exception{
        system = new GoGoPhotoSystem("tagFile.ser", "imageFile.ser");
        Parent root = FXMLLoader.load(getClass().getResource("../scenes/MainScene.fxml"));
        primaryStage.setTitle("GoGoPhoto");
        primaryStage.setScene(new Scene(root, 600, 400));
        primaryStage.setResizable(false);
        primaryStage.show();
    }

    /**
     * This method is called when the program is closed. Save the information stored in the ImageManager and
     * TagManager into imageFile.ser and tagFile.ser.
     * @throws Exception
     */

    @Override
    public void stop() throws Exception {
        system.saveToImageManagerFile("imageFile.ser");
        system.saveToTagManagerFile("tagFile.ser");
    }


}

