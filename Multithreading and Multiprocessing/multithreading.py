import time
import threading

def io_input(task_id, sleep_time = 2)-> None:
    """
    Simulating an I/O bound task using sleep.
    """
    print(f"Task Id:{task_id} starterd ")
    time.sleep(sleep_time)
    print(f"Task Id:{task_id} completed ")

# Comparing the time taken to execute a function using multithreading and serial execution
def run_serial():
    """
    Calculating the time taken to execute a function using serial execution.
    Calling the io_input function 5 times in a loop.
    Each call to the function simulates an I/O bound task by sleeping for 2 seconds.
    """
    start_time = time.time()
    for i in range(5):
        io_input(i, 2)
    end_time = time.time()
    print(f"Time taken to execute the function using serial execution: {end_time - start_time} seconds")

# Multithreading Function
def run_multithreading():
    """
    Calculating the time taken to execute a function using multithreading.
    Calling the io_input function 5 timesin a loop.
    """
    start_time = time.time()
    threads = []
    for i in range(5):
        thread = threading.Thread(target=io_input, args=(i, 2))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Time taken to execute the function using multithreading: {end_time - start_time} seconds")
    print(f"All threads completed:{threads} ")

if __name__ == "__main__":
    """
    Serial execution time = 10 seconds
    Multithreading execution time = 2 seconds
    s_time > m_time 
    Multithreading is faster than serial execution for I/O bound tasks.
    """
    print("Running serial execution")
    run_serial()
    print("Running multithreading")
    run_multithreading()
    print("Multithreading completed")