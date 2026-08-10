def counting_chars(s):
    vowels=0
    consonents=0
    special_chars=0

    for char in s:
        if char in "aeiouAEIOU":
            vowels+=1
        elif char.isalpha():
            consonents+=1
        elif not char.isdigit() and not char.isspace():
            special_chars+=1
    return (vowels,consonents,special_chars)

print(counting_chars("hello world !@"))