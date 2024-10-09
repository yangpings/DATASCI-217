[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16341082)
# Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

```
0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...
```

- Use a function to generate Fibonacci numbers as a list
- Use `with` statements for file operations
- Handle potential file I/O errors with `try`/`except`
- Use command-line arguments (via `argparse`) to specify the upper limit and output file name
 
**Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`**

# Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

- Use command-line arguments to specify the upper limit 
- Implement a function to check if a number is prime
- Import and use the Fibonacci generating function from problem 1 as a module
 
**Task: Find the largest prime Fibonacci number less than 50000**
