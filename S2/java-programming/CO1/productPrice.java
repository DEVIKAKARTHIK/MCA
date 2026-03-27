package java;
import java.util.Scanner;
public class productPrice { 
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Product p1 = new Product();
        Product p2 = new Product();
        Product p3 = new Product();
        p1.setValue(sc);
        p2.setValue(sc);
        p3.setValue(sc);

        if(p1.price < p2.price && p1.price < p3.price) {
            System.out.println(p1.pname+" is having lowset price");
        }
        else if(p2.price < p1.price && p2.price < p3.price) {
            System.out.println(p2.pname+"is having lowset price");
        }
        else
            System.out.println(p3.pname+" is having lowset price");
        sc.close();

    }


}
    //define a class product with data members pcode pname and price.create a 3 objects of the class and find the product having the lowest price


class Product {
    public int pcode;
    public String pname;
    public int price;
    public void setValue(Scanner sc) {
        System.out.println("enter the code:");
        this.pcode = sc.nextInt();
        sc.nextLine();
        System.out.println("enter the name");
        this.pname = sc.nextLine();
        System.out.println("enter the price");
        this.price = sc.nextInt();
    }
   
}