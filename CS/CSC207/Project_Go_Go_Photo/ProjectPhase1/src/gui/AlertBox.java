package gui;

import javafx.stage.*;
import javafx.scene.*;
import javafx.scene.layout.*;
import javafx.scene.control.*;
import javafx.geometry.*;

//The class AlertBox is copied online.

/**
 * AlertBox is a kind of reminder which is always popped out when doing some special.
 * @see Label
 * @see Parent
 * @see Stage
 * @see VBox
 */

public class AlertBox {

    /**
     * This method is called firstly once the main scene is displayed.
     * @param title the title shown in the alert box
     * @param message the message shown in the alert box
     */

    public static void display(String title, String message) {
        Stage window = new Stage();

        //Block events to other windows
        window.initModality(Modality.APPLICATION_MODAL);
        window.setTitle(title);
        window.setHeight(100);
        window.setMinWidth(250);

        Label label = new Label();
        label.setText(message);
        Button closeButton = new Button("Okay, fine");
        closeButton.setOnAction(e -> window.close());

        VBox layout = new VBox(5);
        layout.getChildren().addAll(label, closeButton);
        layout.setAlignment(Pos.CENTER);

        //Display window and wait for it to be closed before returning
        Scene scene = new Scene(layout);
        window.setScene(scene);
        window.showAndWait();
    }

}
