import java.util.*;

class Solution {
    public int evalRPN(String[] tokens) {
        // create the stack
        Stack<Integer> stack = new Stack<>();

        for (String token : tokens) {

            if (token.equals("*")) {
                stack.push(stack.pop() * stack.pop());

            } else if (token.equals("/")) {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b / a);

            }

            else if (token.equals("+")) {
                stack.push(stack.pop() + stack.pop());

            }

            else if (token.equals("-")) {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b - a);

            } else {
                // convert string to integer and store it onto the stack.
                stack.push(Integer.valueOf(token));
            }

        }

        return stack.pop();

    }

}
