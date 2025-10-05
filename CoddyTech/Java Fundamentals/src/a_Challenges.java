import java.util.Scanner;

public class a_Challenges {
    public static void main(String[] args) {
        // Write code here
        int k = 180 ;
        float half = 0.5f ;
        char a = 'c' ;
        // Don't change below this line
        System.out.println("k = " + k);
        System.out.println("half = " + half);
        System.out.println("a = " + a);

        boolean isFun = true ;
        char dollar = '$' ;
        boolean sad = false ;
        String fullName = "John Doe" ;
        // Don't change below this line
        System.out.println("isFun = " + isFun);
        System.out.println("dollar = " + dollar);
        System.out.println("sad = " + sad);
        System.out.println("fullName = " + fullName);

        a = 12;
        int b = 7 ;
        int c = a + b ;
        boolean d = a > c ;
        // Don't change below this line
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        System.out.println("c = " + c);
        System.out.println("d = " + d);

        int p = 99;
        int q = 9;
        int r = 9;

        // Don't change below this line
        boolean dd = ((p - q) > r) && (r == q);
        System.out.println("d = " + dd);

        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        // Don't change above this line

        // Write code here
        int x ;
        if ( num > 5) {
            x = 5 ;
        }
        else {
            x = 0;
        }
        // Don't change below this line
        System.out.println("x = " + x);

        char op = scanner.next().charAt(0);
        int n1 = scanner.nextInt();
        int n2 = scanner.nextInt();
        int res ;
        // Don't change above this line

        // Write code here
        if (op == '+'){
            res = n1 + n2 ;
        }
        else if (op == '-'){
            res = n1 - n2 ;
        }
        else if (op == '*'){
            res = n1 * n2 ;
        }
        else {
            res = 0 ;
        }
        // Don't change below this line
        System.out.println(res);

        System.out.println("Enter your age:") ;
        Scanner sc = new Scanner(System.in);
        int age = sc.nextInt() ;
        int diff = 120 - age ;
        System.out.println(diff);

        int base = sc.nextInt();
        int exp = sc.nextInt();

        int result = 1 ;

        for ( int i = 0 ; i< exp ; i++) {
            result *= base ;

        }

        System.out.println(result);
    }
}
