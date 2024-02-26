package Leetcode;

import java.util.*;

public class permutation {
    public static void main(String[] args) throws Exception {
        System.out.println(permutation("listen", "silent"));

    }

    /**
     * @param a
     * @param b
     * @return boolean
     */
    public static boolean permutation(String a, String b) {
        // convert them to char array because we can't sort string arrays.
        char[] sortedA = a.toCharArray();
        char[] sortedB = b.toCharArray();

        // now we can sort these 2 arrays
        Arrays.sort(sortedA);
        Arrays.sort(sortedB);

        // although we can convert them back to string and perform this same operation,
        // why do extra operations when we can directly compare them in char arrays.
        // this is optimized solution.
        if (Arrays.equals(sortedA, sortedB)) {
            return true;
        }

        return false;
    }

}
