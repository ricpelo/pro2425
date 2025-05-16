public class EjemplosArrays {
    public static void main(String[] args) {
        int[] a = new int[] { 10, 20, 30, 40, 50 };
        String[] s = new String[] { "Hola", null, "María" };
        StringBuilder[] sb = new StringBuilder[] {
            new StringBuilder("Informática"),
            new StringBuilder("Tecnología"),
        };
        int suma;

        for (int i = suma = 0; i < a.length; i++) {
            suma += a[i];
        }

        System.out.println(suma);
        imprimirOrdenInverso(a);

        if (buscar(new int[0], 50)) {
            System.out.println("Sí está el número");
        } else {
            System.out.println("No está el número");
        }

        if (buscar(s, "Pepe")) {
            System.out.println("Sí está la cadena");
        } else {
            System.out.println("No está la cadena");
        }

        if (buscar(sb, new StringBuilder("Informática"))) {
            System.out.println("Sí");
        }


    }

    public static void imprimirOrdenInverso(int[] ar) {
        for (int i = ar.length - 1; i >= 0; i--) {
            System.out.println(ar[i]);
        }
    }

    /* Devuelve true si el valor está dentro del array,
     * o false en caso contrario.
     */
    public static boolean buscar(int[] ar, int valor) {
        for (int i = 0; i < ar.length; i++) {
            if (ar[i] == valor) {
                return true;
            }
        }
        return false;
    }

    public static boolean buscar(CharSequence[] ar, CharSequence valor) {
        for (int i = 0; i < ar.length; i++) {
            if (ar[i] != null && ar[i].toString().equals(valor.toString())) {
                return true;
            }
        }
        return false;
    }
}
