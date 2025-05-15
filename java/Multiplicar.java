public class Multiplicar {
    public static void main(String[] args) {
        final int n = 10;

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i <= 10; i++, vaciar(sb)) {
            sb.append(n);
            sb.append(" x ");
            sb.append(i);
            sb.append(" = ");
            sb.append(n * i);
            System.out.println(sb);
        }
    }

    private static void vaciar(StringBuilder s) {
        s.delete(0, s.length());
    }
}
