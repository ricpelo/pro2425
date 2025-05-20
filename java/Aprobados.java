import java.util.Arrays;

public class Aprobados {
    public static void main(String[] args) {
        String[] nombres = new String[] {
                "Antonio",
                "María",
                "Juan",
                "Ana"
        };
        float[] notas = new float[] { 4.5f, 8.9f, 7.1f, 2.2f };
        String[] alumnosAprobados = aprobados(nombres, notas);
        for (String nombre : alumnosAprobados) {
            System.out.println(nombre);
        }
    }

    public static String[] aprobados(String[] nombres, float[] notas) {
        String[] res;
        int numAprobados = 0;
        if (nombres.length != notas.length) {
            return null;
        }
        for (int i = 0; i < notas.length; i++) {
            if (notas[i] >= 4.5f) {
                numAprobados++;
            }
        }
        res = new String[numAprobados];
        for (int i = 0, j = 0; i < notas.length; i++) {
            if (notas[i] >= 4.5f) {
                res[j++] = nombres[i];
            }
        }
        return res;
    }

    public static String[] aprobados2(String[] nombres, float[] notas) {
        String[] res;
        int numAprobados = 0;
        if (nombres.length != notas.length) {
            return null;
        }
        res = new String[nombres.length];
        for (int i = 0, j = 0; i < notas.length; i++) {
            if (notas[i] > 4.5f) {
                res[j++] = nombres[i];
                numAprobados++;
            }
        }
        // String[] resFinal = new String[numAprobados];
        // System.arraycopy(res, 0, resFinal, 0, numAprobados);
        String[] resFinal = Arrays.copyOf(res, numAprobados);

        return resFinal;
    }
}
