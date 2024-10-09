#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import argparse
def fibonacci(limit):
    # Do something
    seq = [0,1]
    while True:
        next_seq  = seq[-1] + seq[-2]
        if next_seq > limit:
            break
        seq.append(next_seq)
    return seq

def write_to_file(filename, fib):
    try:
        with open(filename, 'w') as f:
            for number in fib:
                f.write(f"{number}\n")
        print(f"Fibonacci sequence written to {filename}")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Generate Fibonacci numbers less than limit and write to a file.")
    parser.add_argument('limit', type=int, help="Upper limit for Fibonacci numbers")
    parser.add_argument('filename', type=str, help="Output file name")

    args = parser.parse_args()

    fib_sequence = fibonacci(args.limit)
    write_to_file(args.filename, fib_sequence)

if __name__ == "__main__":
    # Do stuff here
    main()