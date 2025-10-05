import java.util.Scanner;

public class loops {
    public static void main(String[] args) {
        // Write code here
        int i = 0 ;
        for ( i = 0; i< 10 ; i++){
            System.out.println("hello");
        }

        int i1 = 1 ;
        while(i1 <= 10){
            System.out.println("hello");
            i1++ ;
        }

        for (int i2 = 0; i2 < 100; i2 += 3) {
            // Don't change above this line

            // Write code here
            if ( i2 > 21){
                break ;
            }
            // Don't change below this line
            System.out.println(i2);
        }

        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int i3 = 0 ;
        for ( i3 = 1 ; i3<= num ; i3 ++){
            if (i3 % 3 == 0 || i3 % 7 == 0){
                continue ;
            }
            System.out.println(i3);
        }
    }
}
