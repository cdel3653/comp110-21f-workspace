"""Examples of functions imported elsewhere."""


THE_ANSWER: int = 42


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


if __name__ == "main":
    # python idiom: typically you would call main here
    print(f"helpers.py: {__name__}")
    print("Evaluated as a program")
else:
    # typically not common to do anything in the case where a module is imported
    print("Evalutated as an imported module")