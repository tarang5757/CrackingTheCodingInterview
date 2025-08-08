
"""

solution 1
time complexity: O(n)
space complexitya: o(1)
"""
# def count_subarrays(sales, k):
#     l = 0
#     r = 0
#     bad_days = 0
#     count = 0
#     while r < len(sales):
#         if sales[r] < 10:
#             bad_days += 1
#
#         while bad_days > k:
#             if sales[l] < 10:
#                 bad_days -= 1
#
#             l += 1
#
#
#         count += r - l + 1
#         r += 1



def count_subarrays_2(sales, k):
    l = 0
    r = 0
    window_bad_days = 0
    count = 0

    while r < len(sales):
        must_grow = sales[r] > 10 or window_bad_days < k

        if must_grow:
            if sales[r] < 10:
                window_bad_days += 1

            count += r - l + 1
            r += 1

        else:
            if sales[l] < 10:
                window_bad_days -= 1
            l += 1


    return count










test1 =  [0, 20, 5]
k = 1
print("returned: ", count_subarrays_2(test1, k), "expected: 5")