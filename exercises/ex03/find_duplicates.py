"""Finding duplicate letters in a word."""

__author__ = "730320843"

word_input: str = input("Enter a word: ")
i: int = 0 
counter = 0
while i < len(word_input):
    j: int = 0
    while j < len(word_input):
        if word_input[i] == word_input[j] and i != j:
            counter = counter + 1
        j = j + 1
    i = i + 1
if counter > 0: 
    print("Found duplicate: True")
if counter == 0:
    print("Found duplicate: False")
