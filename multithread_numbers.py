#!/usr/bin/env python3
import random
import time
from threading import Thread, Lock

TOTAL_NUMBERS = 1_000_000
THREAD_COUNT = 4
NUMBERS_PER_THREAD = TOTAL_NUMBERS // THREAD_COUNT

file_lock = Lock()

def write_random_numbers(thread_id):
    with file_lock:
        with open("file_threaded.txt", "a") as f:
            for _ in range(NUMBERS_PER_THREAD):
                f.write(f"{random.random()}\n")
    print(f"Thread-{thread_id} finished writing.")


start_time = time.time()
print("Start Time:", time.strftime("%M:%S", time.localtime(start_time)))

    
threads = []
for i in range(THREAD_COUNT):
    thread = Thread(target=write_random_numbers, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print("End Time:", time.strftime("%M:%S", time.localtime(end_time)))

duration = end_time - start_time
minutes = int((duration % 3600) // 60)
seconds = int(duration % 60)
print(f"Duration: {minutes:02}:{seconds:02}")
