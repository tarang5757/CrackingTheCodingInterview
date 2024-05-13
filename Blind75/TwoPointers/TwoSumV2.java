class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // lets solve this using two-pointer algorithm
        int pointerA = 0;
        int pointerB = numbers.length - 1;

        while (pointerA <= pointerB) {
            int sum = numbers[pointerA] + numbers[pointerB];

            if (sum > target) {
                pointerB -= 1;
            } else if (sum < target) {
                pointerA += 1;
            } else {
                return new int[] { pointerA + 1, pointerB + 1 };
            }

        }
        return new int[] {};
    }

}