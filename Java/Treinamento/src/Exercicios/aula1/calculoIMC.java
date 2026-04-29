package Exercicios.aula1;

public class calculoIMC {
    public static void main(String[] args) {
        double peso = 80.0;
        double altura = 1.80;

        double imc = peso / (altura * altura);

        System.out.println("Peso: " + peso + " kg");
        System.out.println("Altura: " + altura + " m");
        System.out.println("IMC: " + imc);
    }
}
