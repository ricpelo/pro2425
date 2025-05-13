/*
 * Nuestro primer programa Java.
 */

public class Principal {
    public static void main(String[] args) {
        String a = "hola";
        StringBuilder sb = new StringBuilder("pepito");
        sb.append('a');
        CharSequence x = a;
        System.out.println(sb);
    }
}
