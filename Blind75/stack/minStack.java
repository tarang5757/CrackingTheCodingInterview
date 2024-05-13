import java.util.*;

class MinStack {
    // define 2 stacks.
    // one stack to store the inputs and the other stack to store the minimum
    // values.
    Stack<Integer> stack2;
    Stack<Integer> stack;

    public MinStack() {
        stack = new Stack<Integer>();
        stack2 = new Stack<Integer>();
    }

    public void push(int val) {
        if (stack.isEmpty() && stack2.isEmpty()) {
            stack.push(val);
            stack2.push(val);
        } else {
            stack.push(val);
            stack2.push(Math.min(val, stack2.peek()));
        }

    }

    public void pop() {
        if (!stack.isEmpty() && !stack2.isEmpty()) {
            stack.pop();
            stack2.pop();
        }
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return stack2.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */