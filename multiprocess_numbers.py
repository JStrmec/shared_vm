#!/usr/bin/env python3
import random
import time
from multiprocessing import Process, Lock

TOTAL_NUMBERS = 1_000_000
PROCESS_COUNT = 4
NUMBERS_PER_PROCESS = TOTAL_NUMBERS // PROCESS_COUNT

def write_random_numbers(lock, process_id):
    with lock:
        with open("file_multiprocessing.txt", "a") as f:
            for _ in range(NUMBERS_PER_PROCESS):
                f.write(f"{random.random()}\n")
    print(f"Process-{process_id} finished writing.")

start_time = time.time()
print("Start Time:", time.strftime("%M:%S", time.localtime(start_time)))

    
lock = Lock()

processes = []
for i in range(PROCESS_COUNT):
    process = Process(target=write_random_numbers, args=(lock, i))
    processes.append(process)
    process.start()


for process in processes:
    process.join()

end_time = time.time()
print("End Time:", time.strftime("%M:%S", time.localtime(end_time)))

duration = end_time - start_time
minutes = int((duration % 3600) // 60)
seconds = int(duration % 60)
print(f"Duration: {minutes:02}:{seconds:02}")
