"""Drawing forests in a loop."""

__author__ = "730320843"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

forest_depth = int(input("Depth: "))
if forest_depth > 0:
    counter = 0 
    row = 1
    num_trees = 0
    tree_string = ""
    while counter != forest_depth:
        counter = counter + 1
        while num_trees != row:
            tree_string = tree_string + '\U0001F332'
            num_trees = num_trees + 1
        row = row + 1
        print(tree_string)
