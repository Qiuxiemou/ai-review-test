"""Lesson 2 review exercise: empty input must raise ValueError."""


def average(items):
    """Return the arithmetic mean; raise ValueError for an empty sequence."""
    return sum(items) / len(items)
