package Exercicios.aula2;
import java.util.Scanner;

public class AreaRetangulo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite a largura (em cm): ");
        double b = scanner.nextDouble();
        System.out.print("Digite a altura (em cm): ");
        double h = scanner.nextDouble();

        double area = b * h;
        System.out.print("A área do retângulo é igual a " + area + " cm²");

        scanner.close();
    }
}