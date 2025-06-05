import java.util.Arrays;

public class Filtro {
    public static void main(String[] args) {
        Integer[] x = filtrarDistintos(new Integer[] { 4, 2, 1, 3, 5 }, 3);
        String[] y = filtrarDistintos(new String[] { "Pepe", "Juan", "Manolo" }, "Juan");

        System.out.println(Arrays.toString(x));
        System.out.println(Arrays.toString(y));
        System.out.println(Arrays.toString(concatenar(x, y)));
        System.out.println(Arrays.toString(combinar(new String[] { "A", "B", "C", "D" }, new Integer[] { 1, 2 })));
        double[][] matriz = new double[][] {
            {1.2, 2.4, 3.7},
            {4.9, 5.1, 6.0},
            {7.7, 8.24, 9.3},
            {10.5, 11.1, 12.6}
        };
        double[][] resultado = traspuesta(matriz);

        for (double[] fila : resultado) {
            for (double e : fila) {
                System.out.print(e + " ");
            }
            System.out.println();
        }
    }

    public static <T> T[] filtrarDistintos(T[] a, T v) {
        int cuantos = 0;

        for (T e : a) {
            if (e != null && e.equals(v)) {
                cuantos++;
            }
        }

        T[] res = Arrays.copyOf(a, a.length - cuantos);
        int i = 0;

        for (T e : a) {
            if (e == null || !e.equals(v)) {
                res[i++] = e;
            }
        }

        return res;
    }

    public static String[] concatenar(Object[] a1, Object[] a2) {
        String[] res = new String[a1.length * a2.length];
        int i = 0;

        for (Object e1 : a1) {
            for (Object e2 : a2) {
                res[i++] = e1.toString() + e2.toString();
            }
        }

        return res;
    }

    public static Object[] combinar(Object[] a1, Object[] a2) {
        Object[] res = new Object[a1.length + a2.length];
        int i1 = 0, i2 = 0, i = 0;

        // Copia elementos de los dos arrays mientras los dos estén sin agotar:
        while (i1 < a1.length && i2 < a2.length) {
            res[i++] = a1[i1++];
            res[i++] = a2[i2++];
        }

        // // Copia los elementos que faltan del primer array cuando ya se ha
        // // agotado el segundo:
        // for (int x = i1; x < a1.length; x++) {
        //     res[i++] = a1[x];
        // }

        // // Copia los elementos que faltan del segundo array cuando ya se ha
        // // agotado el primero:
        // for (int x = i2; x < a2.length; x++) {
        //     res[i++] = a2[x];
        // }

        System.arraycopy(a1, i1, res, i, a1.length - i1);
        System.arraycopy(a2, i2, res, i, a2.length - i2);

        return res;
    }

    public static int filaMayorSuma(int[][] m) {
        int max = 0;
        int filaMax = 0;

        if (m.length == 0) {
            // throw new IllegalArgumentException("La matriz no puede ser vacía.");
            return -1;
        }

        for (int e : m[0]) {
            max += e;
        }

        for (int fila = 1; fila < m.length; fila++) {
            int suma = 0;
            for (int e : m[fila]) {
                suma += e;
            }
            if (suma > max) {
                max = suma;
                filaMax = fila;
            }
        }

        return filaMax;
    }

    public static double[][] traspuesta(double[][] m) {
        if (m.length == 0 || m[0].length == 0) {
            return new double[0][];
        }

        double[][] res = new double[m[0].length][m.length];

        for (int fila = 0; fila < m.length; fila++) {
            for (int col = 0; col < m[fila].length; col++) {
                res[col][fila] = m[fila][col];
            }
        }

        return res;
    }
}
