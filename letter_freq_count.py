import string
import json

#define text file to open
words_file = open('words_len5.txt', 'r')

#read text file into list
word_list = words_file.read().split('\n')[:-1]

letter_freqs = dict.fromkeys(string.ascii_lowercase, 0)

for word in word_list:

    for letter in word:

        letter_freqs[letter] += 1

sorted_letter_freqs = dict(sorted(letter_freqs.items(),key = lambda x:-x[1]))

json_sorted = json.dumps(sorted_letter_freqs)

file = open("sorted_letter_freqs.json","w")
file.write(json_sorted)
file.close()
