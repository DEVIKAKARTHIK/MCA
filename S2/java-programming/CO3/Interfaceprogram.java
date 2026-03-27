package CO3;


import java.util.Scanner;

// Interface
interface Shape {
    void area();
    void perimeter();
}

// Circle class
class Circle implements Shape {
    double r;

    Circle(double r) {
        this.r = r;
    }

    public void area() {
        System.out.println("Area of Circle: " + (3.14 * r * r));
    }

    public void perimeter() {
        System.out.println("Perimeter of Circle: " + (2 * 3.14 * r));
    }
}

// Rectangle class
class Rectangle implements Shape {
    double l, b;

    Rectangle(double l, double b) {
        this.l = l;
        this.b = b;
    }

    public void area() {
        System.out.println("Area of Rectangle: " + (l * b));
    }

    public void perimeter() {
        System.out.println("Perimeter of Rectangle: " + (2 * (l + b)));
    }
}

// Main class
public class Interfaceprogram  {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("1. Circle");
        System.out.println("2. Rectangle");
        System.out.print("Enter your choice: ");
        int ch = sc.nextInt();

        switch (ch) {
            case 1:
                System.out.print("Enter radius: ");
                double r = sc.nextDouble();
                Circle c = new Circle(r);
                c.area();
                c.perimeter();
                break;

            case 2:
                System.out.print("Enter length and breadth: ");
                double l = sc.nextDouble();
                double b = sc.nextDouble();
                Rectangle rect = new Rectangle(l, b);
                rect.area();
                rect.perimeter();
                break;

            default:
                System.out.println("Invalid choice");
        }

        sc.close();
    }
}