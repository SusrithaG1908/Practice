def first_non_repeating(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch

    return None


print(first_non_repeating("aabbcde"))
print(first_non_repeating("swiss"))
print(first_non_repeating("aabb"))