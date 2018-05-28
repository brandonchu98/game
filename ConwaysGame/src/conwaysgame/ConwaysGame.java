package conwaysgame;

public class ConwaysGame {
    
    public void doTest() {
        ColonyVC vc = new ColonyVC();
        System.out.println("Welcome to the game of life!\n");
        System.out.println("Option for the game of life\n");
        vc.h();
        vc.inputOptions();
    }

    public static void main(String[] args) {
        ConwaysGame c = new ConwaysGame();
        c.doTest();
    }
}