import java.util.Arrays;

public class DuplicadosUnicos {
    public static void main(String[] args) {
        String[] a = filtrarDuplicadosUnicos(new String[] { "a", "b", "a", "c", "d", "d" });
        System.out.println(Arrays.toString(a));
    }

    /**
     * Crea un método genérico llamado filtrarDuplicadosUnicos que
     * reciba un array de elementos y devuelva un nuevo array con
     * los elementos que aparecen exactamente una vez en el array
     * original (elimina todos los duplicados y también los que se
     * repiten).
     *
     * Ejemplo:
     *
     * filtrarDuplicadosUnicos(new String[] { "a", "b", "a", "c", "d", "d" })
     * devuelve { "b", "c" }
     */
    public static <T> T[] filtrarDuplicadosUnicos(T[] a) {
        T[] res = Arrays.copyOf(a, a.length);
        int cont = 0;

        for (T e1 : a) {
            int aux = 0;
            for (T e2 : a) {
                if ((e1 == null && e2 == null) || (e1 != null && e1.equals(e2))) {
                    aux++;
                }
            }
            if (aux == 1) {
                res[cont++] = e1;
            }
        }

        return Arrays.copyOf(res, cont);
    }


    /**
     * Crea un método genérico llamado filtrarDuplicados que
     * reciba un array de elementos y devuelva un nuevo array con
     * los elementos que aparecen repetidos en el array
     * original (en el resultado deben aparecer una sola vez).
     *
     * Ejemplo:
     *
     * filtrarDuplicados(new String[] { "a", "a", "b", "a", "c", "d", "d" })
     * devuelve { "a", "d" }
     */

    public static <T> T[] filtrarDuplicados(T[] a) {
        T[] res = Arrays.copyOf(a, a.length);
        int cont = 0;

        for (T e1 : a) {
            int aux = 0;
            for (T e2 : a) {
                if ((e1 == null && e2 == null) || (e1 != null && e1.equals(e2))) {
                    aux++;
                }
            }
            if (aux > 1) {
                int i;
                for (i = 0; i < cont; i++) {
                    T e2 = res[i];
                    if ((e1 == null && e2 == null) || (e1 != null && e1.equals(e2))) {
                        break;
                    }
                }
                if (i == cont) {
                    res[cont++] = e1;
                }
            }
        }

        return Arrays.copyOf(res, cont);
    }
}
