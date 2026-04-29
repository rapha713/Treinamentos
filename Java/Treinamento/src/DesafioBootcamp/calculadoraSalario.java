package DesafioBootcamp;
import java.util.Scanner;

public class calculadoraSalario {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Nome do funcionário: ");
        String nome = scanner.nextLine();
        System.out.print("Sálario: ");
        double salario = scanner.nextDouble();
        System.out.print("Bônus: ");
        int bonus = scanner.nextInt();

        double salarioFinal = salario + (salario * bonus/100);

        System.out.println("O funcionário " + nome + " recebeu ao final o valor de R$" + salarioFinal);

        scanner.close();
    }
}
