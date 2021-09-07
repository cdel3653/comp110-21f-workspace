"""Counting letters in a string."""

__author__ = "730320843"


letter_search: str = input("What letter do you want to search for? ")
word_searching: str = input("Enter a word: ")
i: int = 0
counter = 0
while i < len(word_searching):
    if word_searching[i] == letter_search: 
        counter = counter + 1
    i = i + 1
print("Count:", counter)