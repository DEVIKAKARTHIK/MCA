package CO2;
import java.util.*;
class search{
    search(){
    System.out.println("enter the size of the array:");
    Scanner sc=new Scanner(System.in);
    int n = sc.nextInt();
    int arr1[] = new int[n];
    System.out.println("enter the elements : ");
    for(int i=0;i<n;i++) {
        arr1[i] = sc.nextInt();
    }
    int arr[]={1,2,3,4,5,6,7,8,9,10};
    System.out.println("Enter the number to be search= ");
    int elem=sc.nextInt();
    System.out.println("number to be search= "+elem);
    int flag=0;
    for(int i=0;i<n;i++){
        if(arr1[i]==elem){
            System.out.println("Element is " +arr1[i]+ " found at "+ (i+1));
            flag=1;
        }
    }
    if(flag==0){
            System.out.println("Element is" +elem+ " not found");
        
    }

        }

}
public class SearchElem {
    public static void main(String args[]){
        search obj=new search();

    }
}
//TO UPPRT,LOWER ,CONCATINATE ,TRIM,SUBSTR,CONCAT