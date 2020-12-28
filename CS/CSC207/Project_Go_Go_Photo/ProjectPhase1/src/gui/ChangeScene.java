package gui;

import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.stage.Stage;

import java.io.IOException;

public interface ChangeScene {
    default void changeScene(Button button, String sceneFile) throws IOException {
        Parent root = FXMLLoader.load(getClass().getResource(sceneFile));
        Stage stage = (Stage) button.getScene().getWindow();
        Scene scene = new Scene(root);
        stage.setScene(scene);
    }
}
