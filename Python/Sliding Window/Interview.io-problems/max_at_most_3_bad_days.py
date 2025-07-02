"""
Problem: Given an array sales, find the most consecutive days with at most 3 bad days (fewer than 10 sales).


Example 1: sales = [0, 14, 7, 9, 0, 20, 10, 0, 10]
Output: 6. There are two 6-day periods with at most 3 bad days, [14, 7, 9, 0, 20, 10] and [9, 0, 20, 10, 0, 10].

Example 2: sales = [10, 10, 10]
Output: 3. All days are good days.

Example 3: sales = [5, 5, 5, 5]
Output: 3. We can include at most 3 bad days.
"""

"""
lets write our thought process
- we will use the resetting window approach to solve this problem.
- we will need to find the longest subarray with at most 3 bad days.
- we will use a sliding window approach to solve this problem.

How this algorithm works:
- we will reset the window when we find a bad day.
- we will keep track of the longest subarray.

Time Complexity: O(n)
Space Complexity: O(1)

"""

def max_at_most_3_bad_days(sales):
    r, l = 0, 0
    curr_max = 0
    window_bad_days = 0


    while r < len(sales):
        can_grow = sales[r] >= 10 or  window_bad_days < 3
        if can_grow:

            if sales[r] < 10:
                window_bad_days += 1
            r += 1
            curr_max = max(curr_max, r - l)

        else:
            if sales[l] < 10:
                window_bad_days -= 1
            l += 1

    return curr_max




test1 = max_at_most_3_bad_days([0, 14, 7, 9, 0, 20, 10, 0, 10])
print("outcome: ", test1, "expected outcome: 6",)

test2 = max_at_most_3_bad_days([10, 10, 10])
print("outcome: ", test2, "expected outcome: 3",)

test3 = max_at_most_3_bad_days([5, 5, 5, 5])
print("outcome: ", test3, "expected outcome: 3",)







