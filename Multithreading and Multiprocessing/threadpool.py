# Multithreading with ThreadPoolExecutor


from concurrent.futures import ThreadPoolExecutor
import time

def print_square(n):
    """Function to print the square of a number."""
    time.sleep(1)  # Simulate a time-consuming task
    return f"The square of {n} is {n * n}"

n = [x*x for x in range(100)]  # List of numbers from 0 to 9
# Create a ThreadPoolExecutor with 3 threads
with ThreadPoolExecutor(max_workers=10) as executor:
    # Map the function to the list of numbers
    results = executor.map(print_square, n)

for result in results:
    print(result)  # This will print None since print_square doesn't return anything