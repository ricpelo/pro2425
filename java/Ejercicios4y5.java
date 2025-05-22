import java.util.Arrays;
import java.util.Scanner;

public class Ejercicios4y5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer[] a = new Integer[5];
        int cuantos = 0;
        int i;

        for (;;) {
            i = sc.nextInt();
            if (i == 0) {
                break;
            }
            if (cuantos >= a.length) {
                a = extender(a);
            }
            a[cuantos++] = i; // auto-boxing
            // assert cuantos <= a.length;
        }

        // Imprimimos el array y fin
        for (i = 0; i < cuantos; i++) {
            System.out.println(a[i]);
        }
    }

    public static <T> T[] extender(T[] ar) {
        return Arrays.copyOf(ar, ar.length + (ar.length / 2));
    }
}
