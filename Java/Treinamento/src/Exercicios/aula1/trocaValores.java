package Exercicios.aula1;

public class trocaValores {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;

        System.out.println("Antes da troca:");
        System.out.println("Valor de a: " + a);
        System.out.println("Valor de b: " + b);

        // Troca dos valores
        int temp = a;
        a = b;
        b = temp;

        System.out.println("Após a troca:");
        System.out.println("Valor de a: " + a);
        System.out.println("Valor de b: " + b);
    }
}
