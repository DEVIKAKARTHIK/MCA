package CO1;
import java.util.Scanner;
public class matrixAddition {
    public static void main(String args[]) {

        int a[][] = new int[2][2];
        int b[][] = new int[2][2];
        int c[][] = new int[2][2];
        Scanner sc = new Scanner(System.in);
        System.out.println("enter array values : ");
        for(int i=0;i<2;i++) {
            for(int j=0;j<2;j++) {
                a[i][j] = sc.nextInt();
            }
        }
        System.out.println("enter b array values : ");
        for(int i=0;i<2;i++) {
            for(int j=0;j<2;j++) {
                b[i][j] = sc.nextInt();
            }
        }

        

        for(int i=0;i<2;i++) {
            for(int j=0;j<2;j++) {
                c[i][j] = a[i][j] + b[i][j];
            }
        }
        for(int i=0;i<2;i++) {
            for(int j=0;j<2;j++) {
                System.out.print(c[i][j]+"\t");
            }
            System.out.println();
        }

        sc.close();
    }
}
// read two matrices from console and perform matrix addition
