def palindromeChecker(s):
    old_count=0
    freq={}
    for ch in s:
        freq[ch] = freq.get(ch,0)+1

    for count in freq.values():
        if count % 2 != 0:
            old_count+=1

    return old_count<=1

print(palindromeChecker("abadbc"))