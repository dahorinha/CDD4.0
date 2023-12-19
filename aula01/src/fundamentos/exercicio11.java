package fundamentos;
import java.util.Scanner;
public class exercicio11 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner (System.in);
		System.out.println("digite um numero de 1 a 7: ");
		double resp = entrada.nextDouble();
		
		if (resp == 1) {
			System.out.println("hoje é domingo");
		}
		if (resp == 2) {
			System.out.println("hoje é segunda");
		}
		if (resp == 3) {
			System.out.println("hoje é terça");
		}
		if (resp == 4) {
			System.out.println("hoje é quarta");
		}
		if (resp == 5) {
			System.out.println("hoje é quinta");
		}
		if (resp == 6) {
			System.out.println("hoje é sexta");
		}
		if (resp == 7) {
			System.out.println("hoje é sabado");
		}
		if (resp != 1 && resp != 2 && resp != 3 && resp !=4 && resp != 5 && resp != 6 && resp != 7){
			System.out.println("valor invalido");
}}}