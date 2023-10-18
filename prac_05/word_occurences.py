"""
CP1404/CP5632 Practical 05
Word Occurrences
Estimate: 20 minutes
Actual: 36 minutes
"""

text = input("Text: ")
words = text.split(" ")
longest_word = ""
text_dictionary = {}

words.sort()

for word in words:
    if word in text_dictionary:
        text_dictionary[word] += 1
    else:
        text_dictionary[word] = 1

for word in text_dictionary:
    if len(word) > len(longest_word):
        longest_word = word

for word, occurrence in text_dictionary.items():
    print(f"{word:{len(longest_word)}} : {occurrence}")
