package Exercicios.aula2;
import java.util.Scanner;

public class converterTemperatura {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite a temperatura em Celsius: ");
        double celsius = scanner.nextDouble();

        double fahrenheit = (celsius * 9/5) + 32;
        System.out.print("A temperatura " + celsius + " em Celsius é igual à " + fahrenheit + " em Fahrenheit");

        scanner.close();
    }
}
