def maxSubstring(s):
    maxLength = 0
    freq = {}

    left = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while freq[s[right]] > 1:
            freq[s[left]] -= 1
            left += 1

        maxLength = max(maxLength, right - left + 1)

    return maxLength


print(maxSubstring("abcdbef"))
print(maxSubstring("bbbb"))