package Exercicios.aula1;

public class conversaoTemperatura {
    public static void main(String[] args) {
        double celsius = 25.0;
        double fahrenheit = 86.0;

        double celsiusToFahrenheit = (celsius * 9 / 5) + 32;
        double fahrenheitToCelsius = (fahrenheit - 32) * 5 / 9;

        System.out.println("Celsius: " + celsius);
        System.out.println("Fahrenheit: " + fahrenheit);
        System.out.println("A temperatura em Celsius " + celsius + " é igual a " + celsiusToFahrenheit + "em Fahrenheit.");
        System.out.println("A temperatura em Fahrenheit " + fahrenheit + " é igual a " + fahrenheitToCelsius + "em Celsius.");
    }
}
