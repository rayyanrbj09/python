# Exception Handling in Python

Exception handling in Python is a mechanism to handle runtime errors, ensuring the normal flow of the program is maintained. Python provides several constructs to handle exceptions.

## Basic Syntax

The basic syntax for exception handling in Python uses the `try`, `except`, `else`, and `finally` blocks.

```python
try:
    # Code that might raise an exception
    pass
except SomeException as e:
    # Code that runs if the exception occurs
    pass
else:
    # Code that runs if no exception occurs
    pass
finally:
    # Code that runs no matter what
    pass
```

## Example

Here is an example of exception handling in Python:

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("No errors occurred.")
finally:
    print("This will run no matter what.")
```

## Common Exceptions

Some common built-in exceptions in Python include:
- `IndexError`
- `KeyError`
- `ValueError`
- `TypeError`
- `FileNotFoundError`

## Raising Exceptions

You can raise exceptions using the `raise` keyword.

```python
if x < 0:
    raise ValueError("x must be non-negative")
```

## Custom Exceptions

You can define custom exceptions by creating a new class that inherits from the `Exception` class.

```python
class CustomError(Exception):
    pass

try:
    raise CustomError("An error occurred")
except CustomError as e:
    print(f"Caught custom exception: {e}")
```

## Conclusion

Exception handling is a crucial part of writing robust Python code. It helps in managing errors gracefully and maintaining the normal flow of the program.