package conwaysgame;

import java.awt.*;
import javax.swing.*;

public class ColonyPanel extends JPanel {
    Colony c;
    
    public ColonyPanel(Colony c) {
        this.c = c;
    }
    
    @Override
    public void paint(Graphics g) {
        super.paint(g);
        int boxWidth = this.getWidth() / c.getBoardSize();
        int boxHeight = (this.getHeight()) / c.getBoardSize();
        for (Coor o : c.cells) {
            int R = (int) (Math.random() * 256);
            int G = (int) (Math.random() * 256);
            int B = (int) (Math.random() * 256);
            Color randomColor = new Color(R, G, B);
            g.setColor(randomColor);
            g.fillRect(o.getX() * boxWidth, (((c.getBoardSize() - 1) - o.getY()) * boxHeight), boxWidth, boxHeight);
        }
    }
}

/*
g.setColor(Color.WHITE);
for (int i = 0; i < c.getBoardSize(); i++) {
    g.drawLine(i * boxWidth, 0, i * boxWidth, this.getHeight());
    g.drawLine(0, i * boxHeight, getWidth(), i * boxHeight);
}

*/
//g.setColor(Color.BLACK);
//g.drawRect(o.getX() * boxWidth, (((c.getBoardSize() - 1) - o.getY()) * boxHeight), boxWidth, boxHeight);