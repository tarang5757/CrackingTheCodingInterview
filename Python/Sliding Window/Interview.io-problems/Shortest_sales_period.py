# Example 1: sales = [5, 10, 15, 5, 10]
# Output: 2. The subarray [10, 15] has over 20 sales.
#
# Example 2: sales = [5, 10, 4, 5, 10]
# Output: 4. [5, 10, 4, 5] and [10, 4, 5, 10] have over 20 sales.
#
# Example 3: sales = [5, 5, 5, 5]
# Output: -1. There is no subarray with more than 20 sales.




def shortest_sales_period(sales):
    r = 0
    l = 0
    window_sum = 0
    shortest_period = float('inf')

    while r < len(sales):
        if window_sum + sales[r] <= 20:
            window_sum += sales[r]
            r += 1

        else:
            shortest_period = min(shortest_period, r - l + 1)
            window_sum -= sales[l]
            l += 1


    return shortest_period if shortest_period != float('inf') else -1


"""
Alternate solution:
def shortest_sales_period(sales):
    r = 0
    l = 0
    window_sum = 0
    shortest_period = float('inf')

    while r < len(sales):
        while window_sum > 20:
            shortest_period = min(shortest_period, r - l)
            window_sum -= sales[l]
            l += 1

        window_sum += sales[r]
        r += 1


    return shortest_period if shortest_period != float('inf') else -1

"""



test1 = shortest_sales_period([5, 10, 15, 5, 10])
print("output: ", test1, "expected outcome: 2")

test2 = shortest_sales_period([5, 10, 4, 5, 10])
print("output: ", test2, "expected outcome: 4")

test3 = shortest_sales_period([5, 5, 5, 5])
print("output: ", test3, "expected outcome: -1")

test4 = shortest_sales_period([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("output: ", test4, "expected outcome: 1")