"""
Max-Subarray-Sum
Problem
Given a non-empty array `arr` of integers (which can be negative), find the non-empty subarray with the maximum sum and return its sum.

```
Example 1: arr = [1, 2, 3, -2, 1]
Output: 6. The subarray with the maximum sum is [1, 2, 3].

Example 2: arr = [1, 2, 3, -2, 7]
Output: 11. The subarray with the maximum sum is the whole array.

Example 3: arr = [1, 2, 3, -8, 7]
Output: 7. The subarray with the maximum sum is [7].

Example 4: arr = [-2, -3, -4]
Output: -2. The subarray cannot be empty.
```

Constraints:
- The length of arr is at most 10^5
- Each element in arr is an integer between -10^3 and 10^3
- The array is non-empty
"""

"""
- lets write our thought process
- we will use the resetting window approach to solve this problem.
- we will need to find the subarray with the maximum sum.
- we will use a sliding window approach to solve this problem.

- we will reset the window when we find a negative element.
- we will keep track of the maximum sum.

Time Complexity: O(n)
Space Complexity: O(1)


"""


def max_subarray_sum(arr):

    # Edge case
    # if the max element of the array is a negative number, return the array immediately
    max_elem = max(arr)
    if max_elem < 0:
        return max_elem


    l, r = 0, 0
    window_sum = 0
    curr_max = 0

    # while window can grow
    while r < len(arr):
        # while the window_sum and curr element is >= 0
        can_grow = window_sum + arr[r] >= 0

        if can_grow:
            window_sum += arr[r]
            r += 1
            curr_max = max(curr_max, window_sum)

        else:
            window_sum = 0
            r += 1
            l = r


    return curr_max


# Testing
test1 = [1, 2, 3, -2, 1]
print("outcome: ", max_subarray_sum(test1), "expected outcome: 6",)

test2 = [1, 2, 3, -2, 7]
print("outcome: ", max_subarray_sum(test2), "expected outcome: 11",)

test3 = [1, 2, 3, -8, 7]
print("outcome: ", max_subarray_sum(test3), "expected outcome: 7",)

test4 = [-2, -3, -4]
print("outcome: ", max_subarray_sum(test4), "expected outcome: -2",)






