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
import model.Image;
import model.ImageManager;
import model.UsedName;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

/**
 * ViewHistoryController is a controller to be responsible for all the operations when buttons are clicked in the
 * ViewRenamingHistoryScene. Turn to AddTagScene when goBack Button is clicked. Pop up an Alert box when backToOldButton
 * is clicked.
 * @see Parent
 * @see Scene
 * @see Stage
 * @see Button
 * @see TableView
 * @see TableColumn
 * @see Image
 */
public class ViewHistoryController implements Initializable, ChangeScene{

    @FXML Button goBack;

    @FXML
    TableView<UsedName> table;

    @FXML
    TableColumn<UsedName, String> usedNameColumn;

    /**
     * This method is called when when goBack Button is clicked. Turn to AddTagScene then.
     */
    public void goBackButtonClicked() throws IOException {
        changeScene(goBack, "../scenes/AddTagScene.fxml");
    }

    /**
     * This method is called when when backToOld Button is clicked. Pop up an Alert box if moving successfully.
     */
    public void backToOldButtonClicked() {
        ImageManager imageManager = Main.system.getImageManager();
        UsedName usedName = table.getSelectionModel().getSelectedItem();
        if (usedName != null) {
            imageManager.backToOldName(getChosenImage(), usedName.getName());
            drawTable(usedNameColumn, "name");
            AlertBox.display("GoGoPhoto", "Success!");
        } else {
            AlertBox.display("GoGoPhoto", "Please select an old name!");
        }
    }

    /**
     * This method is called firstly once the ViewRenaingHistory scene is displayed.
     * @param location default
     * @param resources default
     */

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        drawTable(usedNameColumn, "name");
    }

    /**
     * This method returns the Image associated with the Controller, which is chosen by the user.
     * @return  Image
     */

    private Image getChosenImage() {
        if (LocalOnlyController.getChosenImage() != null) {
            return LocalOnlyController.getChosenImage();
        } else {
            return ListAllController.getChosenImage();
        }
    }

    private void drawTable(TableColumn<UsedName, String> usedNameColumn, String columnName) {
        usedNameColumn.setCellValueFactory(new PropertyValueFactory<>(columnName));
        Image chosenImage = getChosenImage();
        table.setItems(FXCollections.observableArrayList(chosenImage.getRenamingHistory()));
    }
}
