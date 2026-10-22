"""Lesson 1: try changing one value at a time. Run: python example.py."""


def resolve_limit(requested_limit):
    # Like checking requestedLimit === null in our JavaScript example.
    if requested_limit is None:
        return 20
    else:
        # Keep the value the user supplied, including zero.
        return requested_limit


# Python bool(...) is similar to JavaScript Boolean(...).
empty_tasks = []
tasks_with_one_item = ["Learn Python"]

print("Empty task list:", bool(empty_tasks))
print("Task list with one item:", bool(tasks_with_one_item))

# For this example, None means no value was supplied.
print("Missing limit:", resolve_limit(None))
print("Chosen zero:", resolve_limit(0))

# This is a word inside a string, not the boolean value False.
print('Text "false":', bool("false"))
