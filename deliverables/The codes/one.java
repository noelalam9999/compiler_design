import java.io.File;
import java.io.IOException;
import java.io.FileNotFoundException; 
import java.util.Scanner;
import java.util.regex.Pattern;

public class WordCounter {

    private static Scanner input;

    public static void main(String[] args) {
  try{
    String filename = args[0];
    File file = new File(filename);
  
        Scanner myReader = new Scanner(file);
         while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        String str = data;
        String P = args[1];
        String R = args[2];
   str = str.replaceAll(Pattern.quote(P), R);
  
        System.out.println(str);
         }
  }
          catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
      
     
    }
}