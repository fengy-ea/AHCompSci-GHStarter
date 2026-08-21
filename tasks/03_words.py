"""Task 3: list processing practice.

Run with: python3 tasks/03_words.py
Expected final output:
Total words: 5
Longest word: banana
Uppercase words: ['APPLE', 'BANANA', 'PEAR', 'KIWI', 'PLUM']
"""

words = ["apple", "banana", "pear", "kiwi", "plum"]

# TODO: replace 0 with the number of words in the list
total_words = len(words)

# TODO: replace "" with the longest word in the list
length_longest = 0
for i in (words):
    if len(i) > length_longest:
        longest_word = i
        length_longest = len(i)

# TODO: replace [] with a list of the words converted to uppercase
uppercase_words = ['APPLE', 'BANANA', 'PEAR', 'KIWI', 'PLUM']

print(f"Total words: {total_words}")
print(f"Longest word: {longest_word}")
print(f"Uppercase words: {uppercase_words}")
