package CO3;

public class Area {

    // Area of square
    double area(double side) {
        return side * side;
    }

    // Area of rectangle
    double area(double length, double breadth) {
        return length * breadth;
    }

    // Area of circle
    double area(int radius) {
        return 3.14 * radius * radius;
    }
}

public class MethodOverloading{
    public static void main(String[] args) {

        Area obj = new Area();

        System.out.println("Area of Square: " + obj.area(5));
        System.out.println("Area of Rectangle: " + obj.area(4, 6));
        System.out.println("Area of Circle: " + obj.area(3));
    }
} 
