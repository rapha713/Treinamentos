package Exercicios.aula2;
import java.util.Scanner;

public class Multiplicacao {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um número: ");
        int a = scanner.nextInt();

        System.out.print("Digite outro número: ");
        int b = scanner.nextInt();

        double multi = a * b;

        System.out.println("O resultado da multiplicação dos números é de " + multi);

        scanner.close();
    }
}
