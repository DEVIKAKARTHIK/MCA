package CO3;

import java.util.Scanner;

// Student class
class Student {
    int rollNo;
    String name;
    int academicScore;

    void getStudentData(Scanner sc) {
        System.out.print("Enter Roll No: ");
        rollNo = sc.nextInt();
        sc.nextLine();

        System.out.print("Enter Name: ");
        name = sc.nextLine();

        System.out.print("Enter Academic Score: ");
        academicScore = sc.nextInt();
    }
}

// Sports interface
interface Sports {
    int sportsScore = 0;

    void getSportsScore(Scanner sc);
}

// Result class inheriting Student and implementing Sports
class Result extends Student implements Sports {
    int sportsMarks;

    public void getSportsScore(Scanner sc) {
        System.out.print("Enter Sports Score: ");
        sportsMarks = sc.nextInt();
    }

    void display() {
        System.out.println("\n--- Student Result ---");
        System.out.println("Roll No: " + rollNo);
        System.out.println("Name: " + name);
        System.out.println("Academic Score: " + academicScore);
        System.out.println("Sports Score: " + sportsMarks);
    }
}

// Main class
public class Inheritance {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        Result r = new Result();

        r.getStudentData(sc);   // from Student
        r.getSportsScore(sc);   // from Sports

        r.display();

        sc.close();
    }
}