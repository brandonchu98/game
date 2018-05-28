package conwaysgame;

import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;
import javafx.stage.Stage;


public class ColonyFX extends Application {
    Colony c;
    
    public ColonyFX(Colony c) {
        this.c = c;
    }
    
    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle(c.getColonyName());
        Group root = new Group();
        Canvas canvas = new Canvas(600, 600);
        GraphicsContext gc = canvas.getGraphicsContext2D();
        gc.setFill(Color.GREEN);
        double boxWidth = primaryStage.getWidth() / c.getBoardSize();
        double boxHeight = primaryStage.getHeight() / c.getBoardSize();
        c.cells.stream().forEach((o) -> {
            gc.fillRect(o.getX() * boxWidth, (((c.getBoardSize() - 1) - o.getY()) * boxHeight), boxWidth, boxHeight);
        });
        root.getChildren().add(canvas);
        primaryStage.setScene(new Scene(root));
        primaryStage.show();
    }
}
