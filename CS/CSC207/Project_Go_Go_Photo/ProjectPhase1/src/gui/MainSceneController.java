package gui;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.control.Button;
import javafx.stage.*;

import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

/**
 * MainSceneController is a controller to be responsible for all the operations when buttons are clicked in the
 * MainScene. Turn to LogBookScene when logBook Button is clicked, and turn to viewImageScene when viewImage Button
 * is clicked.
 * @see Parent
 * @see Stage
 * @see Button
 */

public class MainSceneController implements Initializable, ChangeScene {

    static String path;
    @FXML Button logBook;
    @FXML Button viewImage;



    /**
     * This method is called when when logBook Button is clicked. Turn to LogBookScene then.
     * @throws IOException
     */
    @FXML
    public void logBookButtonClicked() throws IOException {
        changeScene(logBook, "../scenes/LogScene.fxml");
    }

    /**
     * This method is called when when viewImage Button is clicked. Firstly let the user choose a directory. Set path
     * and turn to ViewImageScene then.
     * @throws IOException
     */
    @FXML
    public void viewImageButtonClicked() throws IOException {
        DirectoryChooser directoryChooser = new DirectoryChooser();
        directoryChooser.setInitialDirectory(new File(System.getProperty("user.home")));
        Stage primaryStage = (Stage) viewImage.getScene().getWindow();
        File selectedDirectory =
                directoryChooser.showDialog(primaryStage);
        if (selectedDirectory != null) {
            changeScene(viewImage, "../scenes/ViewImageScene.fxml");
            setPath(selectedDirectory.getAbsolutePath());
        }

    }

    /**
     * This method returns the path associated with the Controller, which is chosen by the user.
     * @return  String
     */
    public static String getPath() {
        return path;
    }


    /**
     * This method sets the path associated with the Controller, which is chosen by the user.
     */
    public static void setPath(String path) {
        MainSceneController.path = path;
    }


    /**
     * This method is called firstly once the main scene is displayed.
     * @param location default
     * @param resources default
     */
    @Override
    public void initialize(URL location, ResourceBundle resources) {

    }
}