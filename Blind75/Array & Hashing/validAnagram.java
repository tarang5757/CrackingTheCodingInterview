import java.util.*;

public class validAnagram {
    class Solution {
        public boolean isAnagram(String s, String t) {
            // //turn them into character arrays
            char[] array1 = s.toCharArray();
            char[] array2 = t.toCharArray();

            // sort the arrays
            Arrays.sort(array1);
            Arrays.sort(array2);

            // make 2 new string and append the array to convert
            String str1 = new String(array1);
            String str2 = new String(array2);

            // return with the check statement.
            return str1.equals(str2);

            // solution 2
            // if(s.length() != t.length()){
            // return false;
            // }

            // int[] arr1 = new int[26];
            // int[] arr2 = new int[26];

            // for(int i = 0; i < s.length(); i++){
            // char str1 = s.charAt(i);
            // char str2 = t.charAt(i);

            // arr1[str1 - 'a']++;
            // arr2[str2 - 'a']++;
            // }

            // if(Arrays.equals(arr, arr2)){
            // return true;
            // }
            // else{
            // return false;
            // }
            // }

        }
    }

}
