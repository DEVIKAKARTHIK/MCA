import java.util.Scanner;
import Graphics.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        Rectangle r = new Rectangle();
        Triangle t = new Triangle();
        Square s = new Square();
        Circle c = new Circle();

        System.out.print("Enter length and breadth: ");
        double l = sc.nextDouble();
        double b = sc.nextDouble();
        r.area(l, b);

        System.out.print("Enter base and height: ");
        double base = sc.nextDouble();
        double h = sc.nextDouble();
        t.area(base, h);

        System.out.print("Enter side of square: ");
        double side = sc.nextDouble();
        s.area(side);

        System.out.print("Enter radius: ");
        double rad = sc.nextDouble();
        c.area(rad);

        sc.close();
    }
}
