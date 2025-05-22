public class EjemplosArrays {
    public static void main(String[] args) {
        Integer[] a = new Integer[] { 10, 20, 30, 40, 50 };
        String[] s = new String[] { "Hola", null, "María" };
        StringBuilder[] sb = new StringBuilder[] {
            new StringBuilder("Informática"),
            new StringBuilder("Tecnología"),
        };
        int suma;

        Integer i = 5;                   // auto-boxing
        int j = i;                       // auto-unboxing

        Integer k = Integer.valueOf(5);  // boxing
        Integer m = k.intValue();        // unboxing

        System.out.print("La longitud es: ");
        System.out.println(longitud(a));



        for (int z = suma = 0; z < a.length; z++) {
            suma += a[z];
        }

        System.out.println(suma);
        imprimirOrdenInverso(a);
        imprimirOrdenInverso(s);

        if (buscar(new Integer[0], 50)) {
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

    public static <T> void imprimirOrdenInverso(T[] ar) {
        for (int i = ar.length - 1; i >= 0; i--) {
            System.out.println(ar[i]);
        }
    }

    /* Devuelve true si el valor está dentro del array,
     * o false en caso contrario.
     */
    public static <T> boolean buscar(T[] ar, T valor) {
        for (int i = 0; i < ar.length; i++) {
            if (ar[i] != null && ar[i].equals(valor)) {
                return true;
            }
        }
        return false;
    }

    // public static boolean buscar(CharSequence[] ar, CharSequence valor) {
    //     for (int i = 0; i < ar.length; i++) {
    //         if (ar[i] != null && ar[i].toString().equals(valor.toString())) {
    //             return true;
    //         }
    //     }
    //     return false;
    // }

    public static <T> int longitud(T[] a) {
        int res = 0;
        for (T e : a) {
            res += 1;
        }
        return res;
    }
}
