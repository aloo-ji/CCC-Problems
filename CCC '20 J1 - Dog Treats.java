import java.util.*;
class Dog_Treats {
 
  public static void main(String[] args) {
  int S = new Scanner(System.in).nextInt();
  int M = new Scanner(System.in).nextInt();
  int L = new Scanner(System.in).nextInt();
  int HappinessScore = 1 * S + 2 * M + 3 * L;
  if (HappinessScore >= 10) {
    System.out.print("happy");
  }
  else {
     System.out.print("sad");
  }
  }
}

