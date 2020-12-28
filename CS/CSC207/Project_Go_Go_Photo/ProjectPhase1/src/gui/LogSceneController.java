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
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.stage.Stage;
import model.GoGoPhotoSystem;
import model.LogMessage;
import model.LoggerManager;

import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.ResourceBundle;

/**
 * LogSceneController is a controller to be responsible for all the operations when buttons are clicked in the
 * LogScene. Turn to MainScene when goBack Button is clicked.
 * is clicked.
 * @see Parent
 * @see Scene
 * @see Stage
 * @see Button
 * @see TableView
 * @see TableColumn
 */

public class LogSceneController implements Initializable, ChangeScene{

    @FXML Button goBack;

    @FXML
    private TableView<LogMessage> table;


    @FXML
    private TableColumn<LogMessage, String> timeColumn;

    @FXML
    private TableColumn<LogMessage, String> nameColumn;



    /**
     * This method is called when when goBack Button is clicked. Turn to MainScene then.
     * @throws IOException
     */
    @FXML
    public void goBackButtonClicked() throws IOException {
        changeScene(goBack, "../scenes/MainScene.fxml");
    }

    /**
     * This method is called firstly once the LogScene is displayed.
     * @param location default
     * @param resources default
     */
    @Override
    public void initialize(URL location, ResourceBundle resources) {
        timeColumn.setCellValueFactory(new PropertyValueFactory<>("time"));
        nameColumn.setCellValueFactory(new PropertyValueFactory<>("content"));
        ArrayList<LogMessage> logging = new ArrayList<>();
        try {
            logging = LoggerManager.ReadLogMessages(GoGoPhotoSystem.logger, "LogHis.txt");
        } catch (ClassNotFoundException | IOException e) {
            e.printStackTrace();
        }
        table.setItems(FXCollections.observableArrayList(logging));
    }
}
