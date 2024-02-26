package Leetcode;

import java.util.*;

public class permutationOfPalindrome {

    public static void main(String[] args) {
        // FrequencyTable("tarang");

        System.out.println(permutationPalindrome("tactcoapapa"));
    }

    public static boolean permutationPalindrome(String str) {
        // this array will keep count of each character. its a freqncy array of
        // characters
        char[] charArray = new char[128];
        for (int i = 0; i < str.length(); i++) {
            // get the character
            char character = str.charAt(i);
            // putting character-type in the index value of the turns it into ASCII so it
            // finds the position(index) of the ascii value and increaments the count.
            charArray[character]++;
        }

        int count = 0;
        for (int i = 0; i < 128; i++) {
            // we are looking for matches. if theres 2 characters then thats a match. if
            // theres 2 of the same characters thats a match. if theres any even number then
            // thats a match.
            count += charArray[i] % 2;
        }
        // return true if it meets this condition. otherwise return false if its > 1
        return count <= 1;

    }

    // Simple Frequency Hashmap Table.
    /*
     * public static void FrequencyTable(String str) {
     * // create a map
     * HashMap<Character, Integer> myMap = new HashMap<>();
     * 
     * for (int i = 0; i < str.length(); i++) {
     * // value
     * char key = str.charAt(i);
     * if (myMap.containsKey(key)) {
     * myMap.put(key, myMap.get(key) + 1);
     * } else {
     * myMap.put(key, 1);
     * }
     * 
     * }
     * 
     * for (Character key : myMap.keySet()) {
     * System.out.println("Here is the key: " + key + " Value: " + myMap.get(key));
     * }
     * 
     * }
     * 
     */

}
