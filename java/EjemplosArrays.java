public class EjemplosArrays {
    public static void main(String[] args) {
        int[] a = new int[5];
        int[] b = a;

        a[0] = 25;
        a[1] = 33;

        System.out.println(a[0]);
        System.out.println(b[0]);
        System.out.println(a[3]);
    }
}
