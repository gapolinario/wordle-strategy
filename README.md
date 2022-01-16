Find frequency of letters appearing in 5-letter words in the English language

Inspired by Wordle game

List of words in English
https://github.com/dwyl/english-words/blob/master/words_alpha.txt

Then generated 5-letter words with

`grep -E '^[[:alpha:]]{5}$' words_alpha.txt > words_len5.txt`

Two words that contain the 10 most common letters are:
UTILE and SONAR
