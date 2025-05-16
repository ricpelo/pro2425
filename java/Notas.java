public class Notas {
    public static void main(String[] args) {
        float[] notas = new float[] { 4.3f, 7.9f, 2.6f };

        System.out.println(media(notas));
    }

    public static float media(float[] n) {
        float res = 0.0f;

        if (n.length == 0) {
            throw new ArithmeticException("Intento de división entre cero.");
        }

        // for (int i = 0; i < n.length; i++) {
        //     res += n[i];
        // }

        for (float e : n) {
            res += e;
        }

        res /= n.length;

        return Math.round(res * 10) / 10.0f;
    }
}
