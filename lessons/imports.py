"""Examples of Imports."""

from lessons import helpers

# Import using alias
from lessons import helpers as hp

# Import names directly from globals of a module
from lessons.helpers import powerful

print(helpers.powerful(2, 4))
print(helpers.THE_ANSWER)
print(powerful(2, 10))
print(THE_ANSWER)

print(f"imports.py: {__name__}")

