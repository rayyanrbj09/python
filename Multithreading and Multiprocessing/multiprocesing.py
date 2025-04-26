import multiprocessing
import time

# Muliprocessing 
# Simulation CPU bound task using sleep

def square_numbers():
    for i in range(10):
        time.sleep(0.0001)  # Simulating a CPU bound task
        print(f"Square of {i} is {i*i}")
    print("Completed squaring numbers")

def cube_numbers():
    for i in range(10):
        time.sleep(0.0001)  # Simulating a CPU bound task
        print(f"Cube of {i} is {i*i*i}")
    print("Completed cubing numbers")

if __name__ == "__main__":
    """
    Multiprocessing is faster than multithreading for CPU bound tasks.
    """

    start_time = time.time()

    # Creating processes
    process1 = multiprocessing.Process(target=square_numbers)
    process2 = multiprocessing.Process(target=cube_numbers)
    
    # Starting processes
    process1.start()
    process2.start()
    
    # Joining processes
    process1.join()
    process2.join()
    
    end_time = time.time()
    
    print(f"Time taken to execute the function using multiprocessing: {end_time - start_time:.2f} seconds")