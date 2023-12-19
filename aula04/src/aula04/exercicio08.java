package aula04;

public class exercicio08 {

	public static void main(String[] args) {
		String valor = "CDD4.0 - java";
		System.out.println(valor.compareTo("CDD4.0 - java")== 0 ? true : false);
		System.out.println(valor.compareTo("CDD4.0 - JAVA")== 0 ? true : false);
		System.out.println(valor.compareToIgnoreCase("CDD4.0 - JAVA")== 0 ? true : false);
	}
	

}
