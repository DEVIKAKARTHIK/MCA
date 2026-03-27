import java.util.Scanner;

class Publisher {
    String pname;
}

class Book extends Publisher {
    String bname;
}

class Literature extends Book {
    void getData(Scanner sc) {
        System.out.print("Enter Publisher Name: ");
        pname = sc.nextLine();

        System.out.print("Enter Book Name: ");
        bname = sc.nextLine();
    }

    void display() {
        System.out.println("\nPublisher: " + pname);
        System.out.println("Book: " + bname);
    }
}

public class Multilevel {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Literature obj = new Literature();
        obj.getData(sc);
        obj.display();

        sc.close();
    }
}