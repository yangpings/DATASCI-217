#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date

quotes = [
# Create a list of quotes here 34 quotes
"Thomas Edison- Genius is one percent inspiration and ninety-nine percent perspiration.",
"Yogi Berra- You can observe a lot just by watching.",
"Abraham Lincoln- A house divided against itself cannot stand.",
"Johann Wolfgang von Goethe- Difficulties increase the nearer we get to the goal.",
"Byron Pulsifer- Fate is in your hands and no one elses",
"Lao Tzu- Be the chief but never the lord.",
"Carl Sandburg- Nothing happens unless first we dream.",
"Aristotle- Well begun is half done.",
"Yogi Berra-Life is a learning experience, only if you learn.",
"Margaret Sangster- Self-complacency is fatal to progress.",
"Buddha- Peace comes from within. Do not seek it without.",
"Byron Pulsifer- What you give is what you get.",
"Iris Murdoch- We can only learn to love by loving.",
"Karen Clark- Life is change. Growth is optional. Choose wisely.",
"Wayne Dyer- You'll see it when you believe it.",
"Lao Tzu- To lead people walk behind them.",
"William Shakespeare- Having nothing, nothing can he lose.",
"Henry J. Kaiser- Trouble is only opportunity in work clothes.",
"Publilius Syrus- A rolling stone gathers no moss.",
"Napoleon Hill- Ideas are the beginning points of all fortunes.",
"Donald Trump- Everything in life is luck.",
"Lao Tzu- Doing nothing is better than being busy doing nothing.",
"Benjamin Spock- Trust yourself. You know more than you think you do.",
"Confucius- Study the past, if you would divine the future.",
"Sigmund Freud- From error to error one discovers the entire truth.",
"Benjamin Franklin- Well done is better than well said.",
"Ella Williams- Bite off more than you can chew, then chew it.",
"Buddha- Work out your own salvation. Do not depend on others.",
"Benjamin Franklin- One today is worth two tomorrows.",
"Christopher Reeve- Once you choose hope, anythings possible.",
"Albert Einstein- God always takes the simplest way.",
"Charles Kettering- One fails forward toward success.",
"Chinese proverb- Learning is a treasure that will follow its owner everywhere.",
"Socrates- Be as you wish to seem."
]

def get_quote_of_the_day(quotes):
    # Your code here
    #get today's date
    thisdate = date.today()
    #set seed from data to make the quotes fixed
    seed = thisdate.toordinal()
    random.seed(seed)
    #choose a quote from the pool
    todays_quote = random.choice(quotes)
    #return date and the quote
    return f"{thisdate}: {todays_quote}"

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * C:/Users/ericy/PycharmProjects/DATASCI-217/.venv/Scripts/python.exe C:/Users/ericy/PycharmProjects/DATASCI-217/Assignment_3/01-daily_quote.py >> C:/Users/ericy/PycharmProjects/DATASCI-217/Assignment_3/daily_quote.txt