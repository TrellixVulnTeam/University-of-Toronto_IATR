package gui;

import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.image.ImageView;
import javafx.scene.text.Text;
import javafx.stage.DirectoryChooser;
import javafx.stage.Stage;
import model.Image;
import model.ImageManager;
import model.Tag;
import model.UsedName;

import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ResourceBundle;

/**
 * AddTagController is a controller to be responsible for all the operations when buttons are clicked in the
 * AddTagScene. Turn to ListAllScene or LocalOnlyScene when goBack Button is clicked. Turn to ViewHistoryScene when
 * viewHistory Button is clicked. Move the Image to the target directroy when moveImage Button is clicked. Add the tag
 * typed or selected to the Image when the AddTagButton is clicked. And delete the tag from the image if the delete
 * Button is clicked.
 * @see Parent
 * @see Scene
 * @see Stage
 * @see Button
 */

public class AddTagController implements Initializable{

    @FXML Button moveImage;

    @FXML Button viewHistory;

    @FXML Button goBack;

    @FXML Text text;

    @FXML ImageView imageView;

    @FXML TextField newTag;

    @FXML TableView table1;

    @FXML TableView table2;

    @FXML TableColumn tagColumn1;

    @FXML TableColumn tagColumn2;

    /**
     * This method is called when when goBack Button is clicked. Turn to ListAllScene or LocalOnlyScene then based on
     * the former chosen directory.
     */
    public void goBackButtonClicked() {
        Parent root = null;
        try {
            if (ListAllController.getChosenImage() != null) {
                root = FXMLLoader.load(getClass().getResource("../scenes/ListAllScene.fxml"));
            } else {
                root = FXMLLoader.load(getClass().getResource("../scenes/LocalOnlyScene.fxml"));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        Stage stage = (Stage) goBack.getScene().getWindow();
        Scene scene = new Scene(root);
        stage.setScene(scene);
    }

    /**
     * This method is called firstly once the AddTagScene is displayed. Draw the tables for both tags with the image
     * and all the tags, based on all the tag and the Image that the user chooses;
     * @param location default
     * @param resources default
     */
    @Override
    public void initialize(URL location, ResourceBundle resources) {
        //display the name
        text.setText(getChosenImage().getFullName());
        //display the image
        String path = getChosenImage().getPath().toString();
        File f = new File(path);
        javafx.scene.image.Image chosenImage = null;
        try {
            chosenImage = new javafx.scene.image.Image(f.toURL().toString());
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }
        imageView.setImage(chosenImage);
        //display the tags with this image table
        tagColumn2.setCellValueFactory(new PropertyValueFactory<Tag, String>("name"));
        table2.setItems(FXCollections.observableArrayList(getChosenImage().getTagList()));
        //display all the existing tags table
        tagColumn1.setCellValueFactory(new PropertyValueFactory<Tag, String>("name"));
        table1.setItems(FXCollections.observableArrayList(Main.system.getTagManager().getExistingTags()));




    }
    /**
     * This method is called when when viewHistory Button is clicked. Turn to ViewHistoryScene based
     * on the former chosen directory.
     * @throws IOException
     */
    public void viewHistoryButtonClicked() throws IOException {
        Parent newRoot = FXMLLoader.load(getClass().getResource("../scenes/ViewRenamingHistoryScene.fxml"));
        Stage stage = (Stage) viewHistory.getScene().getWindow();
        Scene scene = new Scene(newRoot);
        stage.setScene(scene);
    }

    /**
     * This method is called when when moveImage Button is clicked. Firstly let the user choose a directory. Move the
     * image to that directory then.
     * @throws IOException
     */
    public void moveTheImageButtonClicked() throws IOException {
        DirectoryChooser directoryChooser = new DirectoryChooser();
        directoryChooser.setInitialDirectory(new File(System.getProperty("user.home")));
        Stage primaryStage = (Stage) moveImage.getScene().getWindow();
        File selectedDirectory =
                directoryChooser.showDialog(primaryStage);
        if (selectedDirectory != null) {
            String chosenDirectory = selectedDirectory.getAbsolutePath();
            Main.system.getImageManager().moveImageToDirectory(getChosenImage(), chosenDirectory);
            String message = "   Your image has been moved to \n   " + chosenDirectory + " successfully   ";
            AlertBox.display("GoGoPhoto", message);
            Parent root = FXMLLoader.load(getClass().getResource("../scenes/AddTagScene.fxml"));
            primaryStage.setScene(new Scene(root));

        }
    }

    /**
     * This method is called when when addTag Button is clicked. Add the tag to the image and redraw the table.
     */

    public void addButtonClicked() {
        String tag = newTag.getText();
        Tag getTag = (Tag) table1.getSelectionModel().getSelectedItem();
        ImageManager imageManager = Main.system.getImageManager();
        if (getTag == null) {
            if (tag != null) {
                newTag.setText(null);
                 if (imageManager.foundTag(getChosenImage(), tag)) {
                      String message = "The image have this tag already!";
                      AlertBox.display("GoGoPhoto", message);
                 } else {
                 imageManager.addTagToName(getChosenImage(), tag);
                 }
            } else {
                AlertBox.display("GoGoPhoto", "Please type something!");
            }
        } else {
            if (imageManager.foundTag(getChosenImage(), getTag.getOriginalName())) {
                String message = "The image have this tag already!";
                AlertBox.display("GoGoPhoto", message);
            } else {
                imageManager.addTagToName(getChosenImage(), getTag.getOriginalName());
            }
        }
        tagColumn1.setCellValueFactory(new PropertyValueFactory<UsedName, String>("name"));
        table1.setItems(FXCollections.observableArrayList(Main.system.getTagManager().getExistingTags()));
        tagColumn2.setCellValueFactory(new PropertyValueFactory<Tag, String>("name"));
        table2.setItems(FXCollections.observableArrayList(getChosenImage().getTagList()));
        text.setText(getChosenImage().getFullName());
    }

    /**
     * This method is called when when deleteTag Button is clicked. Delete the tag with the image and redraw the table.
     */
    public void deleteButtonClicked() {
        Tag getTag = (Tag) table2.getSelectionModel().getSelectedItem();
        ImageManager imageManager = Main.system.getImageManager();
        imageManager.deleteTagFromName(getChosenImage(), getTag.getOriginalName());
        tagColumn1.setCellValueFactory(new PropertyValueFactory<UsedName, String>("name"));
        table1.setItems(FXCollections.observableArrayList(Main.system.getTagManager().getExistingTags()));
        tagColumn2.setCellValueFactory(new PropertyValueFactory<Tag, String>("name"));
        table2.setItems(FXCollections.observableArrayList(getChosenImage().getTagList()));
        text.setText(getChosenImage().getFullName());
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
}
