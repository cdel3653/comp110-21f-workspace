"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730320843"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


statement_one = "Be on the alert to recognize your prime at whatever time of your life it may occur."
statement_two = "Your road to glory will be rocky, but fulfilling."
statement_three = "Patience is your alley at the moment. Don’t worry!"
statement_four = "Don’t pursue happiness – create it."
message_range = randint(0, 3)
print("Your fortune cookie says...")
if message_range == 0:
    print(statement_one)
elif message_range == 1:
    print(statement_two)
elif message_range == 2:
    print(statement_three)
elif message_range == 3:
    print(statement_four)
print("Now, go spread positive vibes!")