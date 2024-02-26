package Leetcode;

import java.util.*;

public class URLify {
    public static void main(String[] args) {
        System.out.println(URLify("Mr John Smith"));

    }

    public static String URLify(String str) {

        StringBuilder myString = new StringBuilder();

        for (int i = 0; i < str.length(); i++) {
            char val = str.charAt(i);
            if (val == ' ') {
                myString.append("%20");
            } else {
                myString.append(val);
            }
        }

        return myString.toString();
    }
}
