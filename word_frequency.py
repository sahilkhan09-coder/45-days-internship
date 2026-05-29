# word_frequency.py ---This file counts how many times each word appears or how frequently a word appears

def word_frequency(sentence):

    words = sentence.lower().split()

    frequency = {}

    for word in words:

        if word in frequency:
            frequency[word] += 1

        else:
            frequency[word] = 1

    return frequency


sentence = "Python is a powerful language and Python is fun to learn"

result = word_frequency(sentence)

sorted_result = sorted(
    result.items(),
    key=lambda x: x[1],
    reverse=True
)

for word, count in sorted_result:
    print(f"{word}: {count}")
