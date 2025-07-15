import math


def smallest_range_with_k_elements(arr, k):
    arr.sort()
    l = 0
    r = 0
    best_high = math.inf
    best_low = 0

    while True:
        must_grow  = r - l + 1  < k
        if must_grow:
            print()
            if r == len(arr) - 1:
                break
            r += 1

        else:
            new_diff = arr[r] - arr[l]
            prev_diff = best_high - best_low
            if new_diff < prev_diff:
                best_low = arr[l]
                best_high = arr[r]
            l += 1

    return [best_low, best_high]

test1 = smallest_range_with_k_elements([1, 2, 5, 7, 8], 3)
print("output: ", test1, "expected outcome: [5, 8]")

