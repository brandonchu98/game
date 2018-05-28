package conwaysgame;

import java.util.*;
import java.util.stream.Collectors;

public class Colony {
    public Set<Coor> cells = new HashSet<>();
    private int generationNumber = 0;
    private static int NEXT_COLONY_NUMBER;
    private final int colonyNumber;
    private final int boardSize;
    private final String name;
    
    public Colony(java.lang.String name, int boardSize) {
        this.name = name;
        this.boardSize = boardSize;
        colonyNumber = getNextColonyNumber();
    }
    
    private static int getNextColonyNumber() {
        return NEXT_COLONY_NUMBER++;
    }
    
    public int getBoardSize() {
        return boardSize;
    }

    public int getColonyNumber() {
        return colonyNumber;
    }

    public java.lang.String getColonyName() {
        return name;
    }

    public int getGenerationNumber() {
        return generationNumber;
    }

    public void setCellAlive(int x, int y) {
        cells.add(new Coor(x, y));
    }

    public void setCellDead(int x, int y) {
        cells.remove(new Coor(x, y));
    }

    public void resetColony() {
        cells.clear();
        generationNumber = 0;
    }

    public int getNumberCells() {
        return cells.size();
    }

    public boolean isCellAlive(int x, int y) {
        return cells.contains(new Coor(x, y));
    }
    
    private Set<Coor> calculateCellsToCheck() {
        Set<Coor> cellsToCheck = new HashSet<>();
        int x, y;
        for (Coor c : cells) {
            x = c.getX();
            y = c.getY();
            cellsToCheck.add(new Coor(x - 1, y - 1));
            cellsToCheck.add(new Coor(x - 1, y));
            cellsToCheck.add(new Coor(x - 1, y + 1));
            cellsToCheck.add(new Coor(x, y - 1));
            cellsToCheck.add(new Coor(x, y));
            cellsToCheck.add(new Coor(x, y + 1));
            cellsToCheck.add(new Coor(x + 1, y - 1));
            cellsToCheck.add(new Coor(x + 1, y));
            cellsToCheck.add(new Coor(x + 1, y + 1));
        }
        return cellsToCheck;
    }
    /*
    private Set<Coor> calculateCellsToCheck2() {
        int x, y;
        Set<Coor> cellsToCheck = cells.stream()
                .parallel()
                .map(c -> x = c.getX())
                .map(c -> y = c.getY())
        return cellsToCheck;
    }
    */
    private int cellValue(int x, int y) {
        if (isCellAlive(x, y)) return 1;
        else return 0;
    }
    
    private int countLivingNeighbors(int x, int y) {
        int numAlive = 0;
        numAlive += cellValue(x - 1, y - 1) + cellValue(x - 1, y) + cellValue(x - 1, y + 1);
        numAlive += cellValue(x + 1, y - 1) + cellValue(x + 1, y) + cellValue(x + 1, y + 1);
        numAlive += cellValue(x, y - 1) + cellValue(x, y + 1);
        return numAlive;
    }
    
    private boolean inBounds(int x, int y) {
        return x >= 0 && x < boardSize && y >= 0 && y < boardSize;
    }
    
    private boolean isAliveNextGen(int x, int y) {
        //if(!inBounds(x, y)) return false;
        int numAlive = countLivingNeighbors(x, y);
        if(numAlive < 2 || numAlive > 3) return false;
        if(numAlive == 3) return true;
        return(isCellAlive(x, y));
    }

    public void evolve() {
        Set<Coor> cellsToCheck = calculateCellsToCheck();
        Set<Coor> nextGenCells = cellsToCheck.stream()
                .parallel()
                //.map((c) -> wrapAround(c.getX(), c.getY()))
                .filter(c -> isAliveNextGen(c.getX(), c.getY()))
                .collect(Collectors.toSet());
        cells = nextGenCells;
        generationNumber++;
    }
    
    
    private Coor wrap(Coor c) {
        int x = c.getX();
        int y = c.getY();
        if(x == boardSize) x = 0;
        if(x == -1) x = boardSize - 1;
        if(y == boardSize) y = 0;
        if(y == -1) y = 20;
        Coor c2 = new Coor(x, y);
        return c2;
    }

    private void addDeadCells(Set<Coor> deadCells) {
        for (int y = boardSize - 1; y >= 0; y--) {
            for (int x = 0; x < boardSize; x++) {
                deadCells.add(new Coor(x, y));
            }
        }
    } 
    
    private java.lang.String rowMaker(String row) {
        String[] rows = row.split("(?<=\\G.{"+boardSize+"})");
        String board = Arrays.asList(rows).stream()
                .parallel()
                .map(r -> r + "\n")
                .reduce("", (x, y) -> x + y);
        return board;
    }
    
    @Override
    public java.lang.String toString() {
        System.out.println("Generation " + generationNumber + "\n");
        Set<Coor> deadCells = new LinkedHashSet<>();
        addDeadCells(deadCells);
        String board = deadCells.stream()
                .parallel()
                .map(c -> {if (cells.contains(c)) return "*"; return " ";})
                .reduce("", (x, y) -> x + y);
        return rowMaker(board);
    }
}
