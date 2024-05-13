class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // linkedlist interface
        List<List<Integer>> result = new LinkedList();
        // sort it to keep duplicates adjacent to each other.
        Arrays.sort(nums);

        // iteratation. we -2 so that we can check the last 2 elements using 2 pointers
        // technique.
        for (int i = 0; i < nums.length - 2; i++) {
            // we enter the condition only if i == 0 or if i greater than 0 and there are no
            // duplicates (current element checked with previous element.)
            if (i == 0 || (i > 0 && nums[i] != nums[i - 1])) {
                // 2 pointer method.

                // low pointer. assigning it to i + 1 because we have to check 2 more elements
                // in the array while on current element.
                int low = i + 1;
                // high pointer pointing to the last element in the array.
                int high = nums.length - 1;

                // we are assigning sum = 0 - nums[i] which gives us the difference we need to
                // look for by adding 2 more in the array. This is why we are using 2 pointer to
                // check for the remaining numbers that adds up to 0.
                int sum = 0 - nums[i];

                // iterate as long as low < high
                while (low < high) {

                    // if we find the sum
                    if (nums[low] + nums[high] == sum) {
                        // add it to the array.
                        result.add(Arrays.asList(nums[i], nums[low], nums[high]));
                        // check for duplicates and if we find it, skip by increamenting low by 1
                        while (low < high && nums[low] == nums[low + 1])
                            low++;
                        // same with high.
                        while (low < high && nums[high] == nums[high - 1])
                            high--;
                        // proceed inwards by increamenting high and low pointers.
                        low++;
                        high--;
                    }

                    // if the sum exceeds the target, decreament high pointer
                    else if (nums[low] + nums[high] > sum) {
                        high--;
                    }
                    // if the sum is lower than the target, increament the lower pointer.
                    else {
                        low++;
                    }
                }
            }
        }
        // return the array, we found 0 matching pairs that adds up to 0.
        return result;
    }
}
