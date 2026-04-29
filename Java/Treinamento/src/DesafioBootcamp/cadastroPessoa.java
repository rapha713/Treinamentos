package DesafioBootcamp;
import java.util.Scanner;

public class cadastroPessoa {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("===== CADASTRO =====");

        System.out.print("Nome: ");
        String nome = scanner.nextLine();

        System.out.print("Idade: ");
        int idade = scanner.nextInt();

        scanner.nextLine(); //Limpar buffer

        System.out.print("Cidade: ");
        String cidade = scanner.nextLine();

        System.out.print("Altura (em cm): ");
        int altura = scanner.nextInt();

        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade + " anos");
        System.out.println("Cidade: " + cidade);
        System.out.println("Altura: " + altura + " cm");

        scanner.close();
    }
}