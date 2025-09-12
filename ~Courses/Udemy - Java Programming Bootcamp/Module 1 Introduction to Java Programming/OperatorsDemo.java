// OperatorsDemo.java
public class OperatorsDemo {
    public static void main(String[] args) {
        int a = 12, b = 5;

        // 1. Arithmetic
        System.out.println("Sum=" + (a+b) + ", Diff=" + (a-b) + ", Prod=" + (a*b) + ", Div=" + (a/b) + ", Mod=" + (a%b));

        // 2. Relational
        System.out.println("a>b? " + (a>b) + ", a==b? " + (a==b));

        // 3. Logical
        boolean cond1 = (a>10), cond2 = (b<10);
        System.out.println("cond1 && cond2 = " + (cond1 && cond2));
        System.out.println("cond1 || cond2 = " + (cond1 || cond2));
        System.out.println("!cond1 = " + (!cond1));

        // 4. Bitwise
        System.out.println("a&b = " + (a & b) + ", a|b = " + (a | b) + ", a^b = " + (a ^ b));

        // 5. Increment / Assignment
        int x = 10;
        x += 5;
        System.out.println("x after +=5 = " + x);
        System.out.println("x++ = " + (x++));
        System.out.println("Now x = " + x);
    }
}
