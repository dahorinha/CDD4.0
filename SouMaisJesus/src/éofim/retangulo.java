package éofim;

public class retangulo {
	private double base;
	private double altura;
	private double area;
	private double perimetro;
	
	public retangulo(double base, double altura) {
	this.base = base;
	this.altura = altura;
	
	}

	public double getBase() {
		return base;
	}

	public void setBase(double base) {
		this.base = base;
	}

	public double getAltura() {
		return altura;
	}

	public void setAltura(double altura) {
		this.altura = altura;
	}

	public double getArea() {
		return area;
	}

	public void setArea() {
		this.area = base * altura;
	}

	public double getPerimetro() {
		return perimetro;
	}

	public void setPerimetro() {
		this.perimetro = (base + altura) * 2;
	}
		

	}


