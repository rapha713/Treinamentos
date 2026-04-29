package Exercicios.aula1;

public class conversorMoeda {
    public static void main(String[] args){
        double real = 1000.0;
        double cotacaoDolar = 5.0;

        double dolar = real / cotacaoDolar;

        System.out.println("Reais: " + real);
        System.out.println("Dólares: " + dolar);
    }
}
