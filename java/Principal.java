/*
 * Nuestro primer programa Java.
 */

public class Principal {
    public static void main(String[] args) {
        int i = 0;
        int k;

        if (i < 0) {
            System.out.println("Menor");
        } else if (i == 0) {
            System.out.println("Igual");
        } else {
            System.out.println("Mayor");
        }

        System.out.println(i);

        k = 1;
        String s = "hola" + "pepe";
        String o = s;

        switch (s) {
            case "h":
                System.out.println("Son iguales");
        }
    }
}
