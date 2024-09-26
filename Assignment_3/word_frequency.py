#!/usr/bin/env python3
"""
Word Frequency Counter

This script reads a text file and counts the frequency of each word, ignoring case.

Usage: python word_frequency.py <input_file>


Your task:
- Complete the word_frequency() function to count word frequencies sorted alphabetically
- Test your script on 'alice_in_wonderland.txt'

Hints:
- Use a dictionary to store word frequencies
- Consider using the lower() method to ignore case
- The split() method can be useful for splitting text into words
"""

import sys
def word_frequency(text):
    frequencies = {} # Dictionary to store word frequencies
    # Your code here
    #import string for punctuation
    import string
    # replace text that has - with space so that the words don't go together
    text2= text.replace("-"," ")
    #trim into words without punctuation
    words = text2.translate(str.maketrans('', '', string.punctuation)).lower().split()
    #iterate each word, +1 if a word appears twice, if not register the word and count 1
    for word in words:
        frequencies[word]=frequencies.get(word, 0) + 1
    frequencies = dict(sorted(frequencies.items()))
    return frequencies

# Scaffold for opening a file and running word_frequency() on the contents
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_frequency.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        #windows accept only a utf-8.
        with open(filename, 'r') as file:
            text = file.read() # Read the entire file into a string
        
        frequencies = word_frequency(text)
        
        # Print results
        for word, count in frequencies.items():
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    
    print(f"Word frequencies for '{filename}':")
    print(frequencies)