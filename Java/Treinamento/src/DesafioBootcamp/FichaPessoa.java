package DesafioBootcamp;

public class FichaPessoa {
    public static void main(String[] args){
        String nome = "Raphael Oliveira";
        int idade = 29;
        double altura = 1.79;
        double peso = 88.4;
        String cidade = "Itu";

        System.out.println("FICHA DA PESSOA");
        System.out.println("");

        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("Cidade: " + cidade);
        
        System.out.println("");

        System.out.println("Altura: " + altura + " m");
        System.out.println("Peso: " + peso);
        System.out.println("IMC: " + (peso / (altura * altura)));
    }
}
