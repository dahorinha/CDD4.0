package fundamentos;
import java.util.Arrays;
public class exercicio0 {

	public static void main(String[] args) {
		int Array1[] = {2,5,46,12,34};
		int array2[] = new int[5];
		for(int i=0; i<Array1.length; i++) {
			System.out.println(Array1[i]);
		System.out.println();
		for(int i=4;i>=0;i--) {
			System.out.println(Array1[i]+" ");
			array2[4-i]= Array1[i];
		}
	}
	}
}
