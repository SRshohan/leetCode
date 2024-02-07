# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


def lenghtofLongestSubstring(s):
    start = 0
    uniqueSub = set()
    max_len = 0

    for i in range(len(s)):
        while s[i] in uniqueSub:
            uniqueSub.remove(s[start])
            start += 1

        uniqueSub.add(s[i])


        max_len = max(max_len, i - start + 1)

    return max_len

s = "abcabcbb"
print(lenghtofLongestSubstring(s))

