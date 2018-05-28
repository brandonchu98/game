package conwaysgame;

import java.util.*;

public class ColonyTimer extends TimerTask {
    private ColonyGraphics cgf;
    private int delay;
    private int genNum;
    public Timer timer = new Timer();
    Colony c;
    
    public ColonyTimer(ColonyGraphics cgf, Colony c) {
        this.cgf = cgf;
        this.c = c;
    }
    
    @Override
    public void run() {
        c.evolve();
        cgf.repaint();
        if (c.getGenerationNumber() == genNum) {
            timer.cancel();
        }
    }
    
    public void getGoing(int genNum, int delay) {
        this.genNum = genNum;
        this.delay = delay;
        timer.schedule(this, delay, delay);
    }
}
