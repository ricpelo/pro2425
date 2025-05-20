public class Conversiones {
    public static void main(String[] args) {
        Object o = new Object();
        String s = "Hola";
        String t = "Adiós";
        Object w;
        w = o; // Se puede
        w = s; // Se puede

        t = (String) o; // Sí se puede
        System.out.println(t.length());
    }
}
