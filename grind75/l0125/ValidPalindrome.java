package grind75.l0125;

public class ValidPalindrome {
    public static boolean isValid(String s) {
        boolean rst = true;
        int n = s.length();
        int left = 0;
        int right = n-1;
  
        while (right > left) {
            if (!Character.isLetterOrDigit(s.charAt(right))) {
                right -= 1;
                continue;
            }
            if (!Character.isLetterOrDigit(s.charAt(left))) {
                left += 1;
                continue;
            }
            if (Character.toLowerCase(s.charAt(right)) == Character.toLowerCase(s.charAt(left))) {
                right -= 1;
                left += 1;
            }
            else {
                rst = false;
                break;
            }
        }

        return rst;
    }

    public static void main () {
        System.out.println("Hello Java.");
        System.out.println(isValid("A man, a plan, a canal: Panama"));
        System.out.println(isValid("aa"));
        System.out.println(isValid("aba"));
    }


}


