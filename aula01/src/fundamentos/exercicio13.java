package fundamentos;
import java.util.Scanner;
public class exercicio13 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner (System.in);
		System.out.println("qual o seu sexo?(M/F): ");
		char sexo = entrada.next().charAt(0);
		if (sexo == 'm' || sexo == 'M') {
			System.out.println("masculino");
		}
	
		if (sexo == 'f' || sexo == 'F') {
			System.out.println("feminino");
		}
		if (sexo != 'f' && sexo != 'F' && sexo != 'm' && sexo != 'M' ) {
		System.out.println("INVALIDO");
		}
	}

}
