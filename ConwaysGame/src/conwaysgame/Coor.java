package conwaysgame;

public class Coor {

    int x, y;

    public Coor(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    @Override
    public boolean equals(Object o) {
        Coor c = (Coor) o;
        return (c.getX() == x) && (c.getY() == y);
    }

    public Coor reset(int x, int y) {
        this.x = x;
        this.y = y;
        return this;
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }

    @Override
    public int hashCode() {
        return x * 1000 + y;
    }
}