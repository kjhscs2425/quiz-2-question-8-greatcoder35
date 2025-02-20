"""
8. Use for-loops to print out every 3-letter word that:
starts with one of these letters: c, t,, b
has one of these letters in the middle: a, o
ends with one of these letters: p, t, n

(This should print out 18 words in total)
"""

# YOUR CODE HERE
start_letter = ["c","t","b"]
middle_letter = ["a","o"]
end_letter = ["p","t","n"]
word_count = 1

for first in start_letter:
    for middle in middle_letter:
        for last in end_letter:
            word = first + middle + last
            print(f"{word_count}: {word}")
            word_count += 1