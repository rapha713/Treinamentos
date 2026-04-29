package Exercicios.aula1;

public class consumoCombustivel {
    public static void main(String[] args) {
        double distancia = 96.0;
        double combustivel = 8.0;

        double consumo = distancia / combustivel;

        System.out.println("Consumo médio: " + consumo + " km/l");
    }
}