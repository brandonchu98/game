package conwaysgame;

import java.util.*;

public class ColonyVC {
    Scanner scan = new Scanner(System.in);
    
    private ArrayList<Colony> colonies = new ArrayList<>();
    private ArrayList<ColonyGraphics> frames = new ArrayList<>();
    private ArrayList<ColonyTimer> tasks = new ArrayList<>();
    
    private int xcoor, ycoor;
    private int numMilli = 300;
    private int colonyNumber = 0;
    
    private void c() {
        String name = scan.next();
        int boardSize = Integer.parseInt(scan.next());
        Colony c = new Colony(name, boardSize);
        ColonyGraphics cg = new ColonyGraphics(c);
        colonies.add(c);
        frames.add(cg);
        tasks.add(null);
        colonyNumber = colonies.indexOf(c);
    }
    
    private void a() {
        xcoor = Integer.parseInt(scan.next());
        ycoor = Integer.parseInt(scan.next());
        frames.get(colonyNumber).setVisible(true);
        frames.get(colonyNumber).repaint();
        colonies.get(colonyNumber).setCellAlive(xcoor, ycoor);
    }
    
    private void d() {
        xcoor = Integer.parseInt(scan.next());
        ycoor = Integer.parseInt(scan.next());
        frames.get(colonyNumber).setVisible(true);
        frames.get(colonyNumber).repaint();
        colonies.get(colonyNumber).setCellDead(xcoor, ycoor);
    }
    
    private void e() {
        int genNum = Integer.parseInt(scan.next());
        tasks.add(colonyNumber, new ColonyTimer(frames.get(colonyNumber), colonies.get(colonyNumber)));
        tasks.get(colonyNumber).getGoing(genNum, numMilli);
    }
    
    private void s() {
        int genNum = Integer.parseInt(scan.next());
        for (int x = 0; x < genNum; x++) {
            colonies.get(colonyNumber).evolve();
            System.out.println(colonies.get(colonyNumber).toString());
        }
    }
    
    public void h() {
        System.out.println("c name boardSize- create a new colony with a given name and size");
        System.out.println("u n - use colony number n");
        System.out.println("a xcoor ycoor - set the cell at position (xcoor, ycoor) to be alive");
        System.out.println("d xcoor ycoor - set the cell at position (xcoor, ycoor) to be dead");
        System.out.println("e numGen - evolve the colony by setting all cells to be dead");
        System.out.println("t - wfgh");
        System.out.println("x - reset the colony by setting all cells to be dead");
        System.out.println("w - wrap a cell around the board");
        System.out.println("s - toggle silent evolution");
        System.out.println("p numMilli - set the pause between evolutions to be numMilli milliseconds");
        System.out.println("h - print this table of options");
        System.out.println("i - basic information report");
        System.out.println("q - quit the game\n");
    }
    
    private void i() {
        String use;
        System.out.format("\n" + "%-7s %-10s %-7s %-10s %-10s%n",
                "#", "name", "gen", "living", "board-size\n");
        for (Colony c : colonies) {
            if (colonies.indexOf(c) == colonyNumber) use = "* ";
            else use = "  ";
            System.out.format("%-7s %-10s %-7s %-10s %-10s%n",
                    use + colonies.indexOf(c), c.getColonyName(),
                    c.getGenerationNumber(), c.getNumberCells(), c.getBoardSize());
        }
        System.out.println("");
    }
    
    public void inputOptions() {
        String option;
        colonies.add(new Colony("default", 20));
        tasks.add(null);
        frames.add(new ColonyGraphics(colonies.get(colonyNumber)));
        System.out.print("Option...");
        while (!"q".equals(option = scan.next())) {
            switch (option) {
                case "w": ColonyFX.launch(ColonyFX.class);
                    break;
                case "c": c();
                    break;
                case "u": colonyNumber = Integer.parseInt(scan.next());
                    break;
                case "a": a();
                    break;
                case "d": d();
                    break;
                case "e": e();
                    break;
                case "t": System.out.println(colonies.get(colonyNumber).toString());
                    break;
                case "x": colonies.get(colonyNumber).resetColony();
                    break;
                case "s": s();
                    break;
                case "p": numMilli = Integer.parseInt(scan.next());
                    break;
                case "h": h();
                    break;
                case "i": i();
                    break;
                default: System.out.println(option + " is not an option");
            }
            System.out.print("Option...");
            for (ColonyGraphics cg : frames) {
                cg.dispose();
            }
        }
    }
}

/*
 a 50 50
a 51 50
a 51 52
a 53 51
a 54 50
a 55 50
a 56 50
*/
