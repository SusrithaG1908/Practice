def reverse_words(sentence):

    words = sentence.split()
    result = []

    for i in range(len(words) - 1, -1, -1):
        result.append(words[i])

    return " ".join(result)

print(reverse_words("hello world"))