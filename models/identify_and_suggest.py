def handle_single_insertion(str1, str2):
    for i in range(len(str2)):
        if str1 == str2[:i] + str2[i + 1:]:
            return 1
    return 0

def identify_and_suggest(word_to_check, wordlist):
    list_of_possible_words = []
    for word in wordlist:
        # Single letter insertion
        if len(word) == len(word_to_check) + 1: 
            diff = handle_single_insertion(word_to_check,word)
        # Single letter delition
        elif len(word) + 1 == len(word_to_check): 
            diff = handle_single_insertion(word, word_to_check)
        # Substitution of one letter for another
        elif len(word) == len(word_to_check): 
            diff = sum(1 for char_word, char_wrong_word in zip(word, word_to_check) 
                        if char_word != char_wrong_word)
        else:
            diff = 0

        if diff == 1:
            list_of_possible_words.append(word)

    return list_of_possible_words