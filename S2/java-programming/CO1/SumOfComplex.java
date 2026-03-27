package CO1;
import java.util.Scanner;
class Complex{
    double real,imag;
    Complex(double r,double i){
        real=r;
        imag=i;
    }
    void display(){
        System.out.println(real+" +i "+imag);
    }
}
public class SumOfComplex {
    public static void main(String args[]){
    Scanner sc=new Scanner(System.in);
    Complex arr[] = new Complex[2];
    for(int i=0;i<2;i++){
    System.out.println("enter values : ");
    double re=sc.nextDouble();
    double im=sc.nextDouble();
    arr[i] =new Complex(re,im);
    }

    double sumImage = arr[0].imag + arr[1].imag;
    double sumRead = arr[0].real + arr[1].real;
    Complex c3 = new Complex(sumRead, sumImage);
    c3.display();
    sc.close();
    }
}
