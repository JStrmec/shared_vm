#!/usr/bin/env python3

import time

# Method 1: Read the entire file into memory, then process each row
def method_1(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    with open(output_file, 'w') as outfile:
        for line in lines:
            number = int(line.strip())
            outfile.write(f"{number * 2}\n")


# Method 2: Read one row at a time and process it
def method_2(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            number = int(line.strip())
            outfile.write(f"{number * 2}\n")


# Method 3: Split the file into 2 parts and process each part separately
def method_3(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    mid_index = len(lines) // 2
    part1, part2 = lines[:mid_index], lines[mid_index:]
    
    with open(output_file, 'w') as outfile:
        for part in (part1, part2):
            for line in part:
                number = int(line.strip())
                outfile.write(f"{number * 2}\n")

def calculate_time(start_time, end_time, method):
  duration = end_time - start_time
  minutes = int((duration % 3600) // 60)
  seconds = int(duration % 60)
  milliseconds = int((duration - int(duration)) * 1000)
  print(f"Duration of {method}: {minutes:02}:{seconds:02}.{milliseconds:03}")
  

input_file = "file1.txt"
output_file = "newfile1.txt"
time_format = "%M:%S.%f"
# Run and time Method 1
start_time = time.time()
print("Start Time:", time.strftime(time_format, time.localtime(start_time)))
method_1(input_file, output_file)
end_time = time.time()
print("End Time:", time.strftime(time_format, time.localtime(end_time)))
calculate_time(start_time=start_time, end_time=end_time, method="Method 1")

print("*"*50)
# Run and time Method 2
start_time = time.time()
print("Start Time:", time.strftime(time_format, time.localtime(start_time)))
method_2(input_file, output_file)
end_time = time.time()
print("End Time:", time.strftime(time_format, time.localtime(end_time)))
calculate_time(start_time=start_time, end_time=end_time, method="Method 2")

print("*"*50)
# Run and time Method 3
start_time = time.time()
print("Start Time:", time.strftime(time_format, time.localtime(start_time)))
method_3(input_file, output_file)
end_time = time.time()
print("End Time:", time.strftime(time_format, time.localtime(end_time)))
calculate_time(start_time=start_time, end_time=end_time, method="Method 3")

