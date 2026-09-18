# Skills ? rules for Claude

## Naming
1. Boolean variables, functions and methods must start with "is".
2. Functions and methods must start with a verb.
3. Do not use `and` in names ? it signals multiple responsibilities.
4. Avoid single-character variables.
5. Use clear and descriptive names ? don't save on letters.
6. Numbers must be extracted into named constants.
7. "Service" is a bad name. Use specific roles: "Sender", "Creator", "Reader", etc.
8. Names like "core", "utils" are too abstract ? avoid them.
9. Use verbs with precise semantics:
   - `get` ? retrieve exactly one element; raise an error if there are zero or more than one.
   - `find` ? look up one element or return `None` if not found.
   - `filter` ? return a sequence of elements matching a condition.
   - `read` ? fully consume data from start to finish (file, stream, or external source).
   - `iter` ? lazily iterate over a sequence, yielding elements one by one.

## Scope
1. Everything not used outside a file or class must be private (`_name`).
2. Unused variables in unpacking must be marked as `_`.

## Architecture
1. In Django, business logic must live in `apps/*` or `project_name/*`.
2. A class / function / method must have a single responsibility.
3. If a method "does A and B" ? it is a candidate for decomposition.
4. A class should have one public method. Two ? think twice.
5. If private methods actively call each other ? decomposition is likely needed.
6. Commands and tasks must be thin ? all logic goes into business classes.

## Code style
1. Code must read as a linear story: open ? process ? save ? send.
2. The narrative must be sequential and logical.
3. Consistency matters more than clever or elegant solutions.

## Typing
1. Type annotations are mandatory.
2. Use types deliberately:
   - `list` ? mutable sequence
   - `tuple` ? immutable sequence
   - `set` ? unique elements
   - `frozenset` ? immutable set
3. Use `Optional` (`int | None`) only when genuinely necessary ? and only after explicit confirmation.
4. `*args` / `**kwargs` must be typed.
5. Prefer models (e.g. Pydantic) over raw `dict`.

## Error handling
1. Follow the "fail fast" principle ? fail early, don't mask errors.
2. Do not catch `Exception` without a reason.
3. If you catch an exception ? handle it explicitly or re-raise.
4. `try/except` must be minimal and focused (one statement):
   - `except` ? specific type only
   - `finally` without `except` ? do not use

## General principles
1. Do not implement "future-proof" scenarios without an explicit request.
2. Readability and consistency are the priority.
3. Code must be: clear, linear, predictable, readable without context.

## Decomposition and refactoring
1. Do not create abstractions in advance (no premature abstraction).
2. Write local code first; extract entities only as complexity grows.
3. Extraction is justified only when:
   - it enables reuse
   - it reduces the complexity of the current code
   - it isolates a distinct responsibility
