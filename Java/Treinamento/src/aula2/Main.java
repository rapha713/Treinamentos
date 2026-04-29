package aula2;

import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite seu nome: ");
        String nome = scanner.nextLine();
        //int idade = scanner.nextInt();
        //double altura = scanner.nextDouble();

        System.out.println("Olá, " + nome);

        scanner.close();
    }
}