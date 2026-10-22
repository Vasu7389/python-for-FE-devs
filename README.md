# Python for Frontend Devs 🐍

**Learn Python with JavaScript beside you. Build toward FastAPI, full-stack apps, and interviews in the AI era.**

Already working with JavaScript, TypeScript, or React? This free learning path uses familiar examples to help you learn Python, one small step at a time.

**[Start the free course on Codinn](https://www.codinn.dev/courses/python-for-frontend-devs)** · **[Read lesson 1](https://www.codinn.dev/articles/python-truthiness-versus-javascript)** · **[Explore the roadmap](ROADMAP.md)**

## Start with something familiar

🟦 **JavaScript**

```js
const tasks = [];
console.log(Boolean(tasks)); // true
```

🟩 **Python**

```python
tasks = []
print(bool(tasks))  # False
```

An empty Python list counts as false. An empty JavaScript array counts as true. That's our first idea — the lesson walks through it with examples and practice.

## Run your first example

You'll need Python 3.11 or later and Git. Lesson 1 uses only Python's standard library; there are no packages to install.

```sh
git clone https://github.com/Vasu7389/python-for-FE-devs.git
cd python-for-FE-devs/lessons/001-python-truthiness-versus-javascript
python example.py
```

On Windows, try `py example.py` if you use the Python launcher.

Expected output:

```text
Empty task list: False
Task list with one item: True
Missing limit: 20
Chosen zero: 0
Text "false": True
```

Then open [the practice guide](lessons/001-python-truthiness-versus-javascript/README.md). It includes a starter, clear steps, a hint, and expected results.

## Lessons

| Lesson | Learn | Practice and code |
|---|---|---|
| 01 · Python truthiness vs JavaScript | [Free lesson on Codinn](https://www.codinn.dev/articles/python-truthiness-versus-javascript) | [Exercise](lessons/001-python-truthiness-versus-javascript/README.md) · [Python example](lessons/001-python-truthiness-versus-javascript/example.py) |

**Status:** lesson 1 is available. The rest of the course is in progress. This is not a finished FastAPI application yet.

## Where we're heading

The planned path covers:

- Python fundamentals through JavaScript and TypeScript comparisons.
- HTTP, FastAPI, request validation, async code, and frontend integration.
- PostgreSQL, SQLAlchemy, migrations, authentication, and permissions.
- Background jobs, caching, uploads, and webhooks.
- Docker, CI/CD, monitoring, backups, and safe deployment.
- System design, AI features, debugging, and interview practice.

We'll build toward a team task app with organizations, projects, permissions, files, and notifications. See the [24-module roadmap](ROADMAP.md) for the planned sequence.

## How to use this path

1. Read a lesson on Codinn.
2. Predict what the example will print, then run it.
3. Change one input and see what happens.
4. Try the exercise; use the hint whenever you need it.
5. Explain the idea in your own words. Interview questions are optional practice.

## Help make it clearer

Found an unclear explanation, a broken example, or a useful JavaScript comparison? [Open an issue](https://github.com/Vasu7389/python-for-FE-devs/issues) or read [how to contribute](CONTRIBUTING.md).

If this path helps you, **leave a star ⭐** so other frontend developers can discover it. Watch the repository if you'd like GitHub notifications about updates.

Maintained by [Codinn](https://www.codinn.dev). The published examples and exercises here are free and open source under the [MIT license](LICENSE). Future paid products are separate from this repository.
