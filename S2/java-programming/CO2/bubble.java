package CO2;
import java.util.Scanner;

public class bubble {
    public static void main(String args[]) {
    System.out.println("enter the size of the array:");
    Scanner sc=new Scanner(System.in);
    int n = sc.nextInt();
    int arr1[] = new int[n];
    System.out.println("enter the elements : ");
    for(int i=0;i<n;i++) {
        arr1[i] = sc.nextInt();
    }

        for(int i = 0; i < n - 1; i++) {
            for(int j = 0; j < n - i - 1; j++) {
                if(arr1[j] > arr1[j + 1]) {
                    int temp = arr1[j];
                    arr1[j] = arr1[j + 1];
                    arr1[j + 1] = temp;
                }

        }
    }
    System.out.println("the sorted array is:");
    for(int i=0;i<n;i++) {
        System.out.println(arr1[i]);
    }
}
}
