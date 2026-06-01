public class texteJava {
    int raio;

    // Correção: Adicionado o tipo 'int' para o parâmetro
    public void setRaio(int raio) {
        this.raio = raio;
    }

    // Correção: Mudou de 'int' para 'void', pois o método apenas imprime e não retorna valor
    public void retornarPerimetro() {
        double perimetro = this.raio * 2 * 3.14;
        System.out.println(perimetro);
    }
}