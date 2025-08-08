
"""

Time complexity: o(n)
space complexity: o(1)

"""

import math
def max_good_days_start_and_end(projected_sales, k):
    if not projected_sales:
        return 0

    bad_days = 0

    # find the total number of bad days
    for elem in projected_sales:
        if elem < 10:
            bad_days += 1

    target_window = max(0, bad_days - k)

    if target_window == 0:
        return len(projected_sales)


    l = 0
    r = 0
    min_window = math.inf
    window_bad = 0

    while True:
        must_grow = window_bad < target_window

        if must_grow:

            if r == len(projected_sales):
                break

            if projected_sales[r] < 10:
                window_bad += 1

            r += 1

        else:
            if r - l < min_window:
                min_window = r - l
            if projected_sales[l] < 10:
                window_bad -= 1

            l += 1

    if min_window == math.inf:
        return len(projected_sales)

    return len(projected_sales) - min_window








def run_tests():
    tests = [
        # Example 1 from the book
        ([10, 0, 0, 0, 10, 0, 0, 10], 2, 5),
        # Example 2 from the book
        ([0, 10, 0, 10], 1, 3),
        # Edge case - empty array
        ([], 1, 0),
        # Edge case - k=0
        ([5, 10, 5], 0, 0),
        # Edge case - all good days
        ([10, 10, 10], 1, 3),
        # Edge case - all bad days
        ([5, 5, 5], 2, 2),
    ]

    for projected_sales, k, want in tests:
        got = max_good_days_start_and_end(projected_sales, k)
        print("Outcome: ", got, "Expected: ", want)

run_tests()