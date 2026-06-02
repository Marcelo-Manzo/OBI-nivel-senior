public class texteJava {
    int raio;

    public void setRaio(int raio) {
        this.raio = raio;
    }

    public void retornarPerimetro() {
        double perimetro = this.raio * 2 * 3.14;
        System.out.println(perimetro);
    }

    public static void main(String[] args) {
        texteJava teste = new texteJava();
        teste.setRaio(2);
        teste.retornarPerimetro();
    }
}