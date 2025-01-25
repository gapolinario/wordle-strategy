Find frequency of letters appearing in 5-letter words in the English language

Inspired by Wordle game

List of words in English
https://github.com/dwyl/english-words/blob/master/words_alpha.txt

List of words in PTBR
https://www.ime.usp.br/~pf/dicios/index.html

Then generated 5-letter words with

`grep -E '^[[:alpha:]]{5}$' words_alpha.txt > words_len5.txt`

Two words that contain the 10 most common letters (ENG) are:
UTILE and SONAR

`get-second-word.py` aims at creating a strategy for human players.
To test your second word regex, go to:
https://regex101.com/r/gvkf5V/1

A REGEX for WORDLE is:
```^pr(?=[a-z]*i)(?![a-z]*[outyase])[a-z]{3}$```

(see https://stackoverflow.com/questions/70805802/regex-for-wordle)

About `wordle-fig` folder:
I still cannot get the background to work with the blank cells ([n])
Lookup tikzlibrary(backgrounds)

See past wordles on:
https://wordlearchive.com/450