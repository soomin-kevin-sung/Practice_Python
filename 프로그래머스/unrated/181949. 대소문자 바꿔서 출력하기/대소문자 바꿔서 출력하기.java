import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        var builder = new StringBuilder();
        for (int i = 0 ; i < a.length(); i++) {
            var chr = a.charAt(i);
            builder.append(Character.isLowerCase(chr)
                           ? Character.toUpperCase(chr)
                           : Character.toLowerCase(chr));
        }
        
        System.out.println(builder);
    }
}