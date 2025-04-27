# Multithreading with ThreadPoolExecutor


from concurrent.futures import ThreadPoolExecutor
import time

def print_square(n):
    """Function to print the square of a number."""
    time.sleep(1)  # Simulate a time-consuming task
    return f"The square of {n} is {n * n}"

n = [1, 2, 3, 4, 5]
# Create a ThreadPoolExecutor with 3 threads
with ThreadPoolExecutor(max_workers=3) as executor:
    # Map the function to the list of numbers
    results = executor.map(print_square, n)

for result in results:
    print(result)  # This will print None since print_square doesn't return anything