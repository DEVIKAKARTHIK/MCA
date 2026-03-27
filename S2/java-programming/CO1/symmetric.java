package CO1;
import java.util.Scanner;
public class symmetric {
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter first matrix values : ");
        int arr[][]=new int[2][2];
        for(int i=0;i<2;i++){
            for(int j=0;j<2;j++){
                arr[i][j]=sc.nextInt();
            }
        }
        System.out.println("\nenter second matrix values : ");
        int arr2[][]=new int[2][2];
        for(int i=0;i<2;i++){
            for(int j=0;j<2;j++){
                arr2[i][j]=sc.nextInt();
            }
        }
        boolean flag = true;
        for(int i=0;i<2;i++){
            for(int j=0;j<2;j++){
                if(arr[i][j] != arr2[j][i])
                flag = false;
            }
        }
        if(flag) {
            System.out.println("symmetric");
        }
        else
            System.out.println("asymmetric");
        sc.close();
    }
}
