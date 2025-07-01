
# # Longest Good Day Streak

# Given an array, `sales`, find the most consecutive days with no bad days (fewer than 10 sales).

# ```
# Example 1: sales = [0, 14, 7, 12, 10, 20]
# Output: 3. The subarray [12, 10, 20] has no bad days.

# Example 2: sales = [10, 10, 10]
# Output: 3. All days are good days.

# Example 3: sales = [5, 5, 5]
# Output: 0. There are no good days.
# ```

# Constraints:
# - The length of sales is at most 10^5
# - Each element in sales is a non-negative integer less than 10^3
"""
- we will use the resetting window approach to solve this problem.
- we will need to find the longest subarray with no bad days.
- we will use a sliding window approach to solve this problem.

- we will reset the window when we find a bad day.
- we will keep track of the longest subarray.
"""

def max_no_bad_days(sales):
    l, r = 0, 0
    curr_max = 0

    while r < len(sales):

        if sales[r] >= 10:
            r += 1
            curr_max = max(curr_max, r - l)

        else:
            # Reset the window
            #positions and elements
            l = r + 1
            r = r + 1

    return curr_max







# lets use our test cases
test1 = max_no_bad_days([0, 14, 7, 12, 10, 20])
print("outcome: ", test1, "expected outcome: 3",)

test2 = max_no_bad_days([10, 10, 10])
print("outcome: ", test2, "expected outcome: 3",)

test3 = max_no_bad_days([5, 5, 5])
print("outcome: ", test3, "expected outcome: 0",)

test4 = max_no_bad_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("outcome: ", test4, "expected outcome: 1",)



