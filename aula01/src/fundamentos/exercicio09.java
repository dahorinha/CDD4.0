package fundamentos;
import java.util.Scanner;
public class exercicio09 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner (System.in);
		System.out.println("digite um numero: ");
		double resp = entrada.nextDouble();
			if (resp > 0){
				System.out.println("o numero é positivo");
			}
			else {
				System.out.println("o numero é negativo");
			}

	}

}
