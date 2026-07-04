from collections import Counter
def longestPalindrome(s: str) -> int:
        freq = Counter(s)
        ans = 0
        odd = False

        for count in freq.values():
            if count % 2 == 0:
                ans += count
            else:
                ans += count-1
                odd = True
        
        if odd:
            ans += 1

        return ans
        
print(longestPalindrome("abccccdd"))