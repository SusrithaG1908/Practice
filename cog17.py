def are_anagrams(s1, s2):

    if len(s1) != len(s2):
        return False

    freq1 = {}
    freq2 = {}

    for ch in s1:
        freq1[ch] = freq1.get(ch, 0) + 1

    for ch in s2:
        freq2[ch] = freq2.get(ch, 0) + 1

    return freq1 == freq2


print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))