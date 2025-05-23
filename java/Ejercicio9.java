public class Ejercicio9 {
    public static void main(String[] args) {
        int i = 4;
        short s = 3;
        long l = 9L;

        s = 32767;

        int[][] a = new int[][] {
                { 1, 2, 3 },
                { 4, 5, 6 },
                { 7, 8, 9 }
        };

        for (int fila = 0; fila < a.length; fila++) {
            for (int col = 0; col < a[fila].length; col++) {
                System.out.print(a[fila][col] + " ");
            }
            System.out.println();
        }

        imprimirMatriz(a);
        imprimirMatriz(rellenaCuadrado(7));
    }

    public static void imprimirMatriz(int[][] m) {
        for (int[] fila : m) {
            for (int n : fila) {
                System.out.print(n + " ");
            }
            System.out.println();
        }
    }

    public static int[][] rellenaCuadrado(int n) {
        if (n == 0) {
            return new int[0][];
        }

        int[][] res = new int[n][n];

        for (int i = 0, v = 0; i < res.length; i++) {
            for (int j = 0; j < res[i].length; j++) {
                res[i][j] = ++v;
            }
        }

        return res;
    }
}
