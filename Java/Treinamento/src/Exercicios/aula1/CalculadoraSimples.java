package Exercicios.aula1;

public class CalculadoraSimples {
    public static void main(String[] args){
        int numero1 = 50;
        int numero2 = 8;

        int soma = numero1 + numero2;
        int subtracao = numero1 - numero2;
        int multiplicacao = numero1 * numero2;
        double divisao = (double) numero1 / numero2;

        System.out.println("Número 1: " + numero1);
        System.out.println("Numero 2: " + numero2);
        System.out.println("");
        System.out.println("Resultados:");
        System.out.println("");
        System.out.println("Soma: " + soma);
        System.out.println("Subtração: " + subtracao);
        System.out.println("Multiplicação: " + multiplicacao);
        System.out.println("Divisão: " + divisao);
    }
}
