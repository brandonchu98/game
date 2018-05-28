package conwaysgame;

import java.awt.event.*;
import javax.swing.*;

public class ColonyGraphics extends JFrame {
    JPanel cp;
    
    public ColonyGraphics(Colony c) {
        super();
        add(new ColonyPanel(c));
        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                setVisible(false);
                dispose();
            }
        });
        setTitle(c.getColonyName());
        setSize(700, 700);
    }   
}