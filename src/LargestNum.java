import java.util.Scanner;

public class LargestNum {
    public static void main(String[] args) {
        Scanner Input =new Scanner(System.in);

        int a= Input.nextInt();
        int b= Input.nextInt();
        int c= Input.nextInt();
//
//        int max = 0;
//        a = max;
//        if (max<b){
//            max=b;
//        }
//        if(max<c){
//            max=c;
//        }
//        System.out.println(max);

        System.out.println(Math.max(c,(Math.max(a,b))));
    }
}
