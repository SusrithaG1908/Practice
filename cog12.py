def maxSubstring(s):
    maxLength=0
    seen=set()

    left=0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1

        seen.add(s[right])
        maxLength= max(right-left+1,maxLength)
    return maxLength

print(maxSubstring("abcdbef"))
print(maxSubstring("bbbb"))