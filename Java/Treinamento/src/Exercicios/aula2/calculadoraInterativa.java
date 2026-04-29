package Exercicios.aula2;
import java.util.Scanner;

public class calculadoraInterativa {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um valor: ");
        int valor1 = scanner.nextInt();
        System.out.print("Digite outro valor: ");
        int valor2 = scanner.nextInt();

        int soma = valor1 + valor2;
        int subtracao = valor1 - valor2;
        int multiplicacao = valor1 * valor2;
        double divisao = valor1 / valor2;

        System.out.println("Soma = " + soma);
        System.out.println("Subtração = " + subtracao);
        System.out.println("Multiplicação = " + multiplicacao);
        System.out.println("Divisão = " + divisao);

        scanner.close();
    }
}
