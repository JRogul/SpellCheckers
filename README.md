# SpellCheckers

Project based on youtube video [YT video](https://youtu.be/d-Eq6x1yssU?si=3Tb-zXnzf4Z__VB4)
Data from [Data source](https://www.mit.edu/~ecprice/wordlist.10000)
Implemented algorithms: 
* identify_if_word_in_list.py - function returns True if the given word exists in the words list, and False otherwise.
* identify_and_suggest.py - function iterates through a wordlist to find words that differ from the input word by exactly one single-letter insertion, deletion, or substitution, and returns a list of these similar words.
* levenshtein_distance.py - function recursively calculates the Levenshtein distance between word1 and word2, measuring the minimum number of single-character edits (insertions, deletions, substitutions) needed to transform word1 into word2
