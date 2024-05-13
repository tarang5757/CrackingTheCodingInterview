class Solution {
    public int[] productExceptSelf(int[] nums) {

        int length = nums.length;
        // right array
        int[] right = new int[length];

        // left array
        int[] left = new int[length];

        // result array
        int[] result = new int[length];

        left[0] = 1;
        right[length - 1] = 1;

        for (int i = 1; i < length; i++) {
            int product = nums[i - 1] * left[i - 1];
            left[i] = product;
        }

        for (int i = length - 2; i >= 0; i--) {
            right[i] = nums[i + 1] * right[i + 1];

        }

        for (int i = 0; i < length; i++) {
            result[i] = left[i] * right[i];
        }
        return result;
    }
}