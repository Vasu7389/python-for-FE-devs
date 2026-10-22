# ✍️ Practice · Give a task a title

Let's build one small helper. You can use the lesson while you work.

## 1. Know what we're making

Imagine a user is creating a task. Our helper receives a title and decides what to return:

| Input | Return | Why? |
|---|---|---|
| `None` | `"Untitled"` | No title was supplied. |
| `""` | `""` | The user supplied an empty string. Keep it for this exercise. |
| `"Learn Python"` | `"Learn Python"` | Keep the supplied title. |

An empty string and a missing title are different inputs. We're practicing that difference. A real app might have different rules for empty titles.

## 2. Look at the familiar JavaScript shape

This is how we'll call the helper in JavaScript:

```js
// Imagine resolveTitle is the function you're building.
console.log(resolveTitle(null));           // "Untitled"
console.log(resolveTitle(""));             // "" — an empty string
console.log(resolveTitle("Learn Python")); // "Learn Python"
```

Our Python version will use `None` in place of `null` for the missing title.

## 3. Copy this Python starter

Create a file called `practice.py` in this lesson's folder:

```python
def resolve_title(title):
    # Replace pass with your code.
    pass


print(repr(resolve_title(None)))
print(repr(resolve_title("")))
print(repr(resolve_title("Learn Python")))
```

Here's what the new bits mean:

- `def resolve_title(title):` creates a function with one input, `title`.
- `pass` means "do nothing for now." Replace it with your answer.
- `return` sends a value back from your function.
- `repr()` makes the result easier to see, including quotes around strings. This helps us spot the empty string.

Keep the code inside the function indented by four spaces.

## 4. Make these two decisions

Inside your function:

1. If `title` is `None`, return `"Untitled"`.
2. Otherwise, return `title` as it is.

💡 **Hint:** the lesson's limit example uses `if requested_limit is None:`. You can use the same idea with `title`.

Try writing it before checking an answer.

## 5. Run it and compare

In your terminal:

```sh
python practice.py
```

On Windows, `py practice.py` may also work.

Expected output:

```text
'Untitled'
''
'Learn Python'
```

The middle line is two quotes with nothing between them. That's our empty string — exactly what we wanted.

If you see `None` on every line, your function may still contain `pass`, or it may be missing a `return`. That's a normal first attempt; go back to the two decisions above.

## 6. One tiny experiment — optional

Add this line:

```python
print(repr(resolve_title("0")))
```

Predict the result, then run the file. Remember: `"0"` is text here.

You're done when the three original results match and you can explain why `None` and `""` get different treatment.
