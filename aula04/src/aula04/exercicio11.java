package aula04;
import java.util.StringTokenizer;
import java.util.Scanner;
public class exercicio11 {

	public static void main(String[] args) {
		Scanner texto = new Scanner(System.in);
		System.out.println("escreva um texto: ");
		StringTokenizer resposta = new StringTokenizer(texto.nextLine());
		System.out.println(resposta.countTokens());
		

	}

}
