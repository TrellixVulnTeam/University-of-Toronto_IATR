package gui;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.control.Button;
import javafx.scene.Scene;
import javafx.stage.*;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

/**
 * ViewImageController is a controller to be responsible for all the operations when buttons are clicked in the
 * ViewImageScene. Turn to ListAllScene when listAll Button is clicked, and turn to LocalOnlyScene when localOnly
 * Button is clicked.
 * @see Parent
 * @see Scene
 * @see Stage
 * @see Button
 */
public class ViewImageController implements Initializable, ChangeScene {

    @FXML private Button listAll;

    @FXML private Button localOnly;

    /**
     * This method is called when when listAll Button is clicked. Turn to ViewImage scene then.
     * @throws IOException
     */
    public void listAllButtonClicked() throws IOException {
        changeScene(listAll, "../scenes/ListAllScene.fxml");
    }

    /**
     * This method is called when when localOnly Button is clicked. Turn to LocalOnlyScene then.
     * @throws IOException
     */

    public void localOnlyButtonClicked() throws IOException{
        changeScene(localOnly, "../scenes/LocalOnlyScene.fxml");
    }

    /**
     * This method is called firstly once the ViewImage scene is displayed.
     * @param location default
     * @param resources default
     */

    @Override
    public void initialize(URL location, ResourceBundle resources) {
    }
}
