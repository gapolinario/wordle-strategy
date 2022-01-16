import string
import json

lang="eng"

if lang=="eng":

    #define text file to open
    words_file = open('words_len5.txt', 'r')
    out_file_name = "sorted_letter_freqs.json"

elif lang=="br":

    words_file = open('br_len5.txt', 'r')
    out_file_name = "sorted_letter_freqs_br.json"

#read text file into list
word_list = words_file.read().split('\n')[:-1]

words_file.close()

letter_freqs = dict.fromkeys(string.ascii_lowercase, 0)

for word in word_list:

    for letter in word.lower():

        letter_freqs[letter] += 1

sorted_letter_freqs = dict(sorted(letter_freqs.items(),key = lambda x:-x[1]))

json_sorted = json.dumps(sorted_letter_freqs)

file = open(out_file_name,"w")
file.write(json_sorted)
file.close()
