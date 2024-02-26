package Leetcode;

import java.util.*;

public class Unique {

    /**
     * @param args
     * @throws Exception
     */
    public static void main(String[] args) throws Exception {
        String[] words = { "apple", "car", "little", "Phone", "Tiger", "university" };
        for (String word : words) {
            // System.out.println("Return value for: " + word + " " + checkUnique(word));
            System.out.println("Return value for: " + word + " " + solution2(word));

        }
    }

    // First solution
    public static boolean checkUnique(String str) {
        // create a chars array with 128 characters of memory allocated
        boolean[] chars = new boolean[128];
        // loop through the passed in string
        for (int i = 0; i < str.length(); i++) {
            // create a variable to point to a single character in the array
            char val = str.charAt(i);
            // if that value exists already in the string return false.
            if (chars[val]) {
                return false;
            }
            // set that value to true for unique character
            chars[val] = true;

        }
        // All characters are unique.
        return true;
    }

    public static boolean solution2(String str) {
        // define a hashmap
        HashMap<String, Integer> myMap = new HashMap<>();
        // empty string which will append characters
        String character = "";
        for (int i = 0; i < str.length(); i++) {
            // get each character.
            char val = str.charAt(i);
            // convert character -> String
            character = "" + val;
            // check if map has that string.
            if (myMap.containsKey(character)) {
                // return false if it does
                return false;
            }
            // its unique so add it to hashmap.
            myMap.put(character, i);

        }
        // return true all characters are unique
        return true;

    }

}
