package fundamentos;
import java.util.Arrays;
import java.util.Scanner;
public class exercicio02 {

	public static void main(String[] args) {
		int array1 [] = new int [10];
		int array2 [] = new int [10];
		int array3 [] = new int [10];
		int array4 [] = new int [10];
		Scanner input = new Scanner (System.in);
		
		for (int x = 0; x<array1.length; x++){
		System.out.println("digite um numero: ");
		array1[x]= input.nextInt();
		}
		System.out.println("o array tem os seguintes itens: ");
		for (int z: array1) {
			System.out.println(z+ " ");
		}
		
	}

}
