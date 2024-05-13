class Solution {
    public boolean isPalindrome(String s) {

        // lets convert it into character array first
        char[] arr = s.toCharArray();
        String cleaned = "";

        // loop over the array to clean the string from nonalphanumeric characters such
        // as " , #, $, % etc.."
        for (int i = 0; i < arr.length; i++) {
            if (Character.isDigit(arr[i]) || Character.isLetter(arr[i])) {
                cleaned += arr[i];
            }
        }

        // turn it to lowercase for comparison
        cleaned = cleaned.toLowerCase();

        // two pointers
        int pointerA = 0;
        int pointerB = cleaned.length() - 1;

        while (pointerA <= pointerB) {
            if (cleaned.charAt(pointerA) != cleaned.charAt(pointerB)) {
                return false;
            }
            // increament pointers
            pointerA += 1;
            pointerB -= 1;
        }
        // return true;
        return true;
    }
}