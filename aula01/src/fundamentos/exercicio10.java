package fundamentos;
import java.util.Scanner;
public class exercicio10 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner (System.in);
		System.out.println("digite um numero: ");
		
		double resp = entrada.nextDouble();
		double resp2 = entrada.nextDouble();
		double resp3 = entrada.nextDouble();
		if (resp > resp2 && resp > resp3) {
			System.out.println("o maior é "+resp);
			}
		if (resp2 > resp && resp2 > resp3) {
			System.out.println("o maior é "+resp2);
			}
		if (resp3 > resp && resp3 > resp2) {
			System.out.println("o maior é "+resp3);
		}
		if (resp < resp2 && resp < resp3) {
			System.out.println("o menor é "+resp);
		}
		if (resp2 < resp && resp2 < resp3) {
			System.out.println("o menor é "+resp2);
		}
		if (resp3 < resp && resp3 < resp2) {
			System.out.println("o menor é "+resp3);
		}
	}

}
