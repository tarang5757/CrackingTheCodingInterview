# # Unique Best Seller Streak

# Given the array `best_seller` and a number `k` with `1 ≤ k ≤ len(sales)`, return whether there is any k-day period where each day has a **different** best-selling title.

# ```
# Example 1: best_seller = ["book3", "book1", "book3", "book3", "book2", "book3", "book4", "book3"], k = 3
# Output: True. There is a 3-day period without a repeated value: ["book2", "book3", "book4"].

# Example 2: best_seller = ["book3", "book1", "book3", "book3", "book2", "book3", "book4", "book3"], k = 4
# Output: False. There are no 4-day periods without a repeated value.

# Example 3: best_seller = ["book1", "book2", "book3"], k = 3
# Output: True. The entire array has no repeated values.
# ```

# Constraints:
# - The length of best_seller is at most 10^5
# - Each book title has length at most 100
# - 1 ≤ k ≤ len(best_seller)

"""
- In this problem, we will need find k-day period where each book is different.
Given this example,
# Example 1: best_seller = ["book3", "book1", "book3", "book3", "book2", "book3", "book4", "book3"] = 3
output: 3

- we see that k-day period is 3 because there are 3 books with different titles at indexes(4, 5, 6) =
[book2, book3, book4]

- How do we solve this problem?
- we will need to use a hashmap to store the counts of the book.
- everytime the book is not found in map, we will decrease its count.
- when the count goes to 0, we will remove it from map.

- add the book.

"""

def find_kday_period(best_seller, k):
    l, r = 0, 0
    books_count = {}

    while r < len(best_seller):
        # Add current book to the window
        if best_seller[r] not in books_count:
            books_count[best_seller[r]] = 1
        else:
            books_count[best_seller[r]] += 1

        # If window size equals k
        if r - l + 1 == k:
            # Check if we have k unique books
            if len(books_count) == k:
                return True

            # Remove the leftmost book from window
            books_count[best_seller[l]] -= 1
            if books_count[best_seller[l]] == 0:
                del books_count[best_seller[l]]
            l += 1

        r += 1
    return False



# ```
# Example 1: best_seller = ["book3", "book1", "book3", "book3", "book2", "book3", "book4", "book3"], k = 3
# Output: True. There is a 3-day period without a repeated value: ["book2", "book3", "book4"].

# Example 2: best_seller = ["book3", "book1", "book3", "book3", "book2", "book3", "book4", "book3"], k = 4
# Output: False. There are no 4-day periods without a repeated value.

# Example 3: best_seller = ["book1", "book2", "book3"], k = 3
# Output: True. The entire array has no repeated values.

test1 = find_kday_period(["book3", "book1", "book3", "book3", "book2", "book3", "book4", "book3"], 3)
print("outcome: ", test1, "expected outcome: True",)

test2 = find_kday_period(["book3", "book1", "book3", "book3", "book2", "book3", "book4", "book3"], 4)
print("outcome: ", test2, "expected outcome: False",)

test3 = find_kday_period(["book1", "book2", "book3"], 3)
print("outcome: ", test3, "expected outcome: True",)



"""
Goal: Find if any slice of length k has all unique items.

Why sliding window? Because checking every slice from scratch is too slow.

How sliding window works here:

Keep two pointers: left (l) and right (r).

Move right pointer forward, adding books to a frequency map.

Once window size is k, check if number of unique books == k.

Then remove the book at left pointer from the map, move left forward.

Repeat until you find a unique window or reach the end.

Key insight:
The frequency map size = number of unique books in current window.
So if size == k, all are unique.

Important detail: Remove books from map when their count drops to zero to keep map accurate.

Complexity:
Time: O(n) because each book enters and leaves the window once.
Space: O(k) for the map.

Use this pattern whenever:
You need to check conditions on fixed-size subarrays and want to do it efficiently.





"""






