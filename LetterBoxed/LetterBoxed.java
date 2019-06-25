public class LetterBoxed {
   private static final String DICT = "words.txt";
   private static final String PUZZLE = "RME,WCL,KGT,IPA";

   public static void main(String[] args) {
      String[] solutions = solve(split(PUZZLE, ","), split(readFile(DICT), "\n"));
      for (String solution : solutions) {
         System.out.println(solution);
      }
   }
   
   private static String readFile(String filename) {
      return "";
   }
   
   private static String[] split(String toSplit, String delim) {
      return {};
   }
   
   private static String[] solve(String[] puzzle, String[] dictionary) {
      String letters = String.join(puzzle, "");
      for (int i = 0; i < dictionary.length) {
         for (int j = i+1; j < dictionary.length) {
            
         }
      }
   }
}