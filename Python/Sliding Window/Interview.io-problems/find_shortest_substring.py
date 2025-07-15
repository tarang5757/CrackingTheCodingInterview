from collections import Counter


from collections import Counter

def find_shortest_substring(s1, s2):
    """
    Find the length of the shortest substring in s1 that contains all characters in s2 (including duplicates).
    If no such substring exists, return -1.

    Example:
        s1 = "helloworld", s2 = "well"
        Output: 5  -> because "ellow"

    Parameters:
        s1 (str): Source string
        s2 (str): Target string

    Returns:
        int: Length of shortest valid substring, or -1 if not found
    """

    # Step 1: Count required characters
    target_map = Counter(s2)
    window_count = {}

    # Step 2: Initialize pointers and counters
    l = 0
    have, need = 0, len(target_map)
    min_len = float('inf')
    r = 0

    # Step 3: Expand right pointer
    while r < len(s1):
        curr = s1[r]

        # If current character is needed, update window count
        if curr in target_map:
            window_count[curr] = window_count.get(curr, 0) + 1
            if window_count[curr] == target_map[curr]:
                have += 1

        # Step 4: Shrink from the left while valid
        while have == need:
            # Update result
            window_size = r - l + 1
            min_len = min(min_len, window_size)

            # Remove leftmost character from window
            left_char = s1[l]
            if left_char in target_map:
                window_count[left_char] -= 1
                if window_count[left_char] < target_map[left_char]:
                    have -= 1
            l += 1  # Shrink left

        r += 1


    # Step 5: Return result
    return min_len if min_len != float('inf') else -1

















test1 = find_shortest_substring("helloworld", "well")
print("outcome: ", test1, "expected outcome: 5",)

test2 = find_shortest_substring("helloworld", "weelll")
print("outcome: ", test2, "expected outcome: -1",)

test3 = find_shortest_substring("ADOBECODEBANC", "ABC")
print("outcome: ", test3, "expected outcome: 4",) # "BANC"



