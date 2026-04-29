package aula2;

import java.util.Scanner;

public class idade {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite seu nome: ");
        String nome = scanner.nextLine();

        System.out.print("Digite sua idade: ");
        int idade = scanner.nextInt();

        System.out.println("Olá " + nome + ", sua idade é de " + idade + " anos.");

        scanner.close();
    }
}