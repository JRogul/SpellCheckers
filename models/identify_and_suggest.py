def handle_single_insertion(str1, str2):
    for i in range(len(str2)):
        if str1 == str2[:i] + str2[i + 1:]:
            return 1
    return 0

def identify_and_suggest(WRONG_WORD, wordlist):
    list_of_possible_words = []
    for word in wordlist:
        
        if len(word) == len(WRONG_WORD) + 1: 
            diff = handle_single_insertion(WRONG_WORD,word)
        # Single letter delition
        elif len(word) + 1 == len(WRONG_WORD): 
            diff = handle_single_insertion(word, WRONG_WORD)
        # Substitution of one letter for another
        elif len(word) == len(WRONG_WORD): 
            diff = sum(1 for char_word, char_wrong_word in zip(word, WRONG_WORD) 
                        if char_word != char_wrong_word)
        else:
            diff = 0

        if diff == 1:
            list_of_possible_words.append(word)

    return list_of_possible_words