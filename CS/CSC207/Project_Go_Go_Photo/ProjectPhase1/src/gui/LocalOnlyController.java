package gui;

import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.stage.Stage;
import model.ExistingImage;
import model.Image;

import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.ResourceBundle;

/**
 * LocalOnlyController is a controller to be responsible for all the operations when buttons are clicked in the
 * LocalOnlyScene. Turn to AddTagScene when chooseButton is clicked. And turn to MainScene when goBack
 * Button is clicked.
 * @see Parent
 * @see Scene
 * @see Stage
 * @see Button
 * @see Image
 */
public class LocalOnlyController implements Initializable, ChangeScene {

    private static Image chosenImage;

    @FXML Button chooseButton;

    @FXML Button goBackButton;

    @FXML
    private TableView<ExistingImage> table;

    @FXML
    private TableColumn<ExistingImage, String> nameColumn;

    @FXML
    private TableColumn<ExistingImage, String> pathColumn;

    /**
     * This method is called firstly once the LocalOnly scene is displayed. Draw the table based on the images in
     * the directory that the user chooses;
     * @param location default
     * @param resources default
     */

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        nameColumn.setCellValueFactory(new PropertyValueFactory<>("name"));
        pathColumn.setCellValueFactory(new PropertyValueFactory<>("path"));
        String path = MainSceneController.getPath();
        ArrayList<ExistingImage> allImages;
        try {
            allImages = Main.system.getDirectoryManager().findLocalImages(path);
            table.setItems(FXCollections.observableArrayList(allImages));
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
    /**
     * This method is called when when choose Button is clicked. Make the Image chosen by the user associated with the
     * contronller. Turn to AddTag scene then.
     * @throws IOException
     */
    public void chooseButtonClicked() throws IOException {
        ExistingImage selected = table.getSelectionModel().getSelectedItem();
        Image targetImage = Main.system.getImageManager().foundImage(selected.getPath());
        if (targetImage == null) {
            chosenImage = new Image(selected.getImageName(), selected.getImageType(), selected.getPath());
            Main.system.getImageManager().addImage(chosenImage);
        } else {
            chosenImage = targetImage;
        }
        changeScene(chooseButton, "../scenes/AddTagScene.fxml");
    }

    /**
     * This method is called when when goBack Button is clicked. Turn to MainScene then.
     */
    public void goBackButtonClicked() throws IOException {
        chosenImage = null;
        changeScene(goBackButton, "../scenes/MainScene.fxml");
    }

    /**
     * This method returns the Image associated with the Controller, which is chosen by the user.
     * @return  Image
     */
    public static Image getChosenImage() {
        return chosenImage;
    }
}
