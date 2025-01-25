"""
What word is best as the second word?
This can be done with the same algorihtm as for the first word,
The idea here is to build a database for human wordle players,
to use in different cases, given the output of the first word

See wordle_bot_second_word.txt with a few entries,
Column 1: first guess of the NYT wordle bot
Column 2: second guess of the NYT wordle bot
Column 3: The solution
Column 4: Return of the game for the first word,
0 = black, 1 = yellow, 2 = green
Column 5: Date this word was the solution of the NYT puzzle
Column 6: A regex to identify all valid words in a second guess
"""

import re

first = 'crane'

with open('words_len5.txt','r') as f:
    text = f.read()

print(text)

