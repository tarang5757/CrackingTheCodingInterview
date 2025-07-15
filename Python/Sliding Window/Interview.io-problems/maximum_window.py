"""
#
# Example 1: projected_sales = [5, 5, 15, 0, 10], k = 12
# Output: 3. We can reach 3 consecutive good days in two ways: boosting days 0 and 1 to reach 10 sales each, or boosting day 3 to reach 10 sales.

# Example 2: projected_sales = [5, 5, 15, 0, 10], k = 15
# Output: 4. We can boost days 1 and 3 to reach 10 sales each.

# Example 3: projected_sales = [0, 0, 0], k = 29
# Output: 2. We can use all boosts on days 0 and 1 to reach 10 sales each.
# ```
"""


def maximum_window(projected_sales, k):
    return 0





test1 = maximum_window([5, 5, 15, 0, 10], 12)
print("outcome: ", test1, "expected outcome: 3",)

test2 = maximum_window([5, 5, 15, 0, 10], 15)
print("outcome: ", test2, "expected outcome: 4",)

test3 = maximum_window([0, 0, 0], 29)
print("outcome: ", test3, "expected outcome: 2",)