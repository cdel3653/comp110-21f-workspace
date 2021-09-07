"""Repeating a beat in a loop."""

__author__ = "730320843"


user_beat = input("What beat do you want to repeat? ")
user_amount = int(input("How many times do you want to repeat it? "))
counter = 0
x = user_beat
if user_amount <= 0:
    print("No beat...")
else:
    user_beat2 = "" 
    while counter < user_amount: 
        user_beat2 = user_beat2 + x
        if counter < user_amount - 1:
            user_beat2 = user_beat2 + " "
        counter = counter + 1
    print(user_beat2)
