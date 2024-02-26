package Leetcode;

import java.util.*;

import static org.junit.Assert.*;

import org.junit.Test;
import org.junit.FixMethodOrder;
import org.junit.runners.MethodSorters;

public class LeetcodeTester {

    @Test
    public void validPalindrome() {
        String actual = "a man, a plan, a canal: Panama";
        assertEquals(true, Leetcode.validPalindrome.isPalindrome(actual));
    }

    @Test
    public void TwoSome() {
        int[] arr1 = { 1, 2 };
        int[] arr2 = { 1, 3 };

        // Test Arrays
        int[] numbers = { 2, 7, 11, 15 };
        int[] numbers2 = { 2, 3, 4 };
        int target = 9;
        int target2 = 6;

        assertArrayEquals(arr1, Leetcode.TwoSum2.twoSum(numbers, target));
        assertArrayEquals(arr2, Leetcode.TwoSum2.twoSum(numbers2, target2));

    }
}
