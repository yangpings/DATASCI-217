#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!

import argparse
from fibonnaci import fibonacci
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_fibonacci(limit):
    fib_sequence = fibonacci(limit)
    prime_fibs = [num for num in fib_sequence if prime(num)]
    if prime_fibs:
        return max(prime_fibs)
    else:
        return None

def main():
    parser = argparse.ArgumentParser(description="Find the largest prime Fibonacci number less than limit.")
    parser.add_argument('limit', type=int, help="Upper limit for Fibonacci numbers")
    args = parser.parse_args()
    largest_prime = largest_prime_fibonacci(args.limit)

    if largest_prime:
        print(f"The largest prime Fibonacci number less than {args.limit} is: {largest_prime}")
    else:
        print(f"No prime Fibonacci numbers found below {args.limit}.")

if __name__ == "__main__":
    main()