package fundamentos;
import java.util.Scanner;
public class exercicio12 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner (System.in);
		System.out.println("digite uma nota: ");
		double nota1 = entrada.nextDouble();
		double nota2 = entrada.nextDouble();
		double media = ((nota1 + nota2) / 2);
		System.out.println("a media é: " +media);
		

	}

}
