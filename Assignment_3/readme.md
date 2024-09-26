[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16170876)
1. **Daily Quote Generator:** Select a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

	Your task:
	1. Complete the get_quote_of_the_day() function
	2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

	Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
2. **Word Frequency Counter:** Read a text file (example code included) and count the frequency of each word, ignoring case.
	Usage: `python word_frequency.py <input_file>`  
	
	Your task: Complete the word_frequency() function to count word frequencies sorted alphabetically. Run the script on '02-sample.txt'.
	
	Hints:
	- Use a dictionary to store word frequencies
	- Consider using the `lower()` method to ignore case
	- The `split()` method can be useful for splitting text into words
3. **Maximum Product of 13 Adjacent Digits:** Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
	
	Your task: Complete the find_greatest_product() function to solve the problem.
	
	Hints:
	- You can iterate through the string using a for loop and string slicing
	- Keep track of the maximum product as you go through the loooong number
	- (Optional) Convert characters to integers using `int()`
