"""Examples of using lists in a simple 'game'."""


from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or  rolls[len(rolls) - 1 ] != 1:
    rolls.append(randint(1, 6))

print(rolls)

# Remove an item form the list by its inded ("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# Sum the valus of our rolls!
i: int = 0
sum: int = 0
while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1

    print(f"Total score: {sum}")

# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# # Access an individual item
# print(rolls[0])
# print(rolls[1])

# # Access the length of a list (nuumber of times)
# print(len(rolls))

# # Access last item of list
# print(rolls[len(rolls) - 1])
