public class EjemplosArrays {
    public static void main(String[] args) {
        int[] a = new int[] { 10, 20, 30, 40, 50 };
        String[] s = new String[] { "Hola", null, "María" };
        int suma;

        for (int i = suma = 0; i < a.length; i++) {
            suma += a[i];
        }

        System.out.println(suma);
        imprimirOrdenInverso(a);
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
        ;
    }
}
