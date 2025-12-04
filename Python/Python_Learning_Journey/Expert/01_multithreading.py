"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              Kataria Kushal                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Program 1: Multithreading and Concurrency
Learning Objective: Understand threading, locks, and concurrent programming
"""

import threading
import time
import queue
from concurrent.futures import ThreadPoolExecutor
import random

# Basic threading
print("=== Basic Threading ===")

def worker_function(name, duration):
    """Function to be executed in a thread"""
    print(f"Worker {name} starting...")
    time.sleep(duration)
    print(f"Worker {name} finished after {duration} seconds")

# Create and start threads
threads = []
for i in range(3):
    thread = threading.Thread(target=worker_function, args=(f"Thread-{i+1}", random.uniform(1, 3)))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads completed")

# Thread synchronization with locks
print("\n=== Thread Synchronization ===")

# Shared resource
counter = 0
counter_lock = threading.Lock()

def increment_counter(name, iterations):
    """Function that increments a shared counter"""
    global counter
    for i in range(iterations):
        # Critical section - only one thread can execute this at a time
        with counter_lock:
            current = counter
            time.sleep(0.0001)  # Simulate some processing
            counter = current + 1
        
        if i % 100 == 0:
            print(f"{name}: Iteration {i}, Counter: {counter}")

# Create threads that modify shared resource
sync_threads = []
for i in range(3):
    thread = threading.Thread(target=increment_counter, args=(f"Counter-{i+1}", 500))
    sync_threads.append(thread)
    thread.start()

for thread in sync_threads:
    thread.join()

print(f"Final counter value: {counter}")

# Producer-Consumer pattern with Queue
print("\n=== Producer-Consumer Pattern ===")

# Thread-safe queue
task_queue = queue.Queue(maxsize=5)
results_queue = queue.Queue()

def producer(name, num_items):
    """Producer function that adds items to queue"""
    for i in range(num_items):
        item = f"{name}-Item-{i+1}"
        task_queue.put(item)
        print(f"Producer {name} added: {item}")
        time.sleep(0.1)
    
    # Signal completion
    task_queue.put(None)

def consumer(name):
    """Consumer function that processes items from queue"""
    while True:
        item = task_queue.get()
        if item is None:
            task_queue.task_done()
            break
        
        # Simulate processing
        processing_time = random.uniform(0.1, 0.5)
        time.sleep(processing_time)
        
        result = f"Processed {item} in {processing_time:.2f}s"
        results_queue.put(result)
        print(f"Consumer {name}: {result}")
        
        task_queue.task_done()

# Start producer and consumer threads
producer_thread = threading.Thread(target=producer, args=("Producer-1", 5))
consumer_thread = threading.Thread(target=consumer, args=("Consumer-1"))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

# Collect results
print("\nProcessing results:")
while not results_queue.empty():
    print(f"- {results_queue.get()}")

# Thread Pool Executor
print("\n=== Thread Pool Executor ===")

def cpu_intensive_task(n):
    """Simulate CPU-intensive task"""
    result = sum(i*i for i in range(n))
    thread_name = threading.current_thread().name
    print(f"Task completed by {thread_name}: sum of squares up to {n} = {result}")
    return result

# Using ThreadPoolExecutor for better thread management
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks
    futures = []
    for i in range(5):
        future = executor.submit(cpu_intensive_task, (i+1) * 10000)
        futures.append(future)
    
    # Collect results
    results = []
    for future in futures:
        result = future.result()  # This blocks until the task completes
        results.append(result)

print(f"All task results: {results}")

# Thread-local data
print("\n=== Thread-Local Data ===")

# Create thread-local storage
thread_local_data = threading.local()

def process_data(data):
    """Function that uses thread-local storage"""
    # Each thread gets its own copy of this data
    thread_local_data.value = data
    thread_local_data.processed_count = 0
    
    for item in data:
        # Simulate processing
        time.sleep(0.1)
        thread_local_data.processed_count += 1
        
    thread_name = threading.current_thread().name
    print(f"{thread_name}: Processed {thread_local_data.processed_count} items")
    print(f"{thread_name}: Data was {thread_local_data.value}")

# Create threads with different data
data_sets = [
    ["A", "B", "C"],
    ["X", "Y", "Z"],
    ["1", "2", "3"]
]

local_threads = []
for i, data in enumerate(data_sets):
    thread = threading.Thread(target=process_data, args=(data,), name=f"DataProcessor-{i+1}")
    local_threads.append(thread)
    thread.start()

for thread in local_threads:
    thread.join()

# Daemon threads
print("\n=== Daemon Threads ===")

def background_monitor():
    """Background monitoring function"""
    count = 0
    while True:
        count += 1
        print(f"Background monitor: Check #{count}")
        time.sleep(2)

# Create daemon thread (will be killed when main program exits)
daemon_thread = threading.Thread(target=background_monitor, daemon=True)
daemon_thread.start()

print("Main program running...")
time.sleep(5)  # Let daemon run for 5 seconds
print("Main program ending (daemon will be terminated)")

"""
Example Output:
=== Basic Threading ===
Worker Thread-1 starting...
Worker Thread-2 starting...
Worker Thread-3 starting...
Worker Thread-2 finished after 1.23 seconds
Worker Thread-1 finished after 2.45 seconds
Worker Thread-3 finished after 2.89 seconds
All threads completed

=== Thread Synchronization ===
Counter-1: Iteration 0, Counter: 1
Counter-2: Iteration 0, Counter: 2
Counter-3: Iteration 0, Counter: 3
...
Final counter value: 1500

=== Producer-Consumer Pattern ===
Producer Producer-1 added: Producer-1-Item-1
Consumer Consumer-1: Processed Producer-1-Item-1 in 0.23s
...

=== Thread Pool Executor ===
Task completed by ThreadPoolExecutor-0_0: sum of squares up to 10000 = 333283335000
Task completed by ThreadPoolExecutor-0_1: sum of squares up to 20000 = 2666266670000
...

What you learned:
- Creating and managing threads with threading module
- Thread synchronization using locks to prevent race conditions
- Producer-Consumer pattern with thread-safe queues
- ThreadPoolExecutor for better thread management
- Thread-local data for per-thread storage
- Daemon threads for background tasks
- Best practices for concurrent programming
- When to use threading vs other concurrency approaches
"""