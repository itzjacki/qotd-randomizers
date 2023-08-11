import java.util.Random;

void main() {
  String[]names={"Yngve","Robin","Vegard","Sunniva"};
  Random rng=new Random();
  int randomIndex=rng.nextInt(names.length);
  System.out.println("Den heldige vinneren er: "+names[randomIndex]+"!");
}
