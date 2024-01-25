def handle_single_insertion(str1, str2):
    for i in range(len(str2)):
        if str1 == str2[:i] + str2[i + 1:]:
            return 1
    return 0

def identify_and_suggest(word, wordlist):
    list_of_possible_words = []
    for word in wordlist:
        # Single letter insertion
        if len(word) == len(word) + 1: 
            diff = handle_single_insertion(word,word)
        # Single letter delition
        elif len(word) + 1 == len(word): 
            diff = handle_single_insertion(word, word)
        # Substitution of one letter for another
        elif len(word) == len(word): 
            diff = sum(1 for char_word, char_word in zip(word, word) 
                        if char_word != char_word)
        else:
            diff = 0

        if diff == 1:
            list_of_possible_words.append(word)

    return list_of_possible_words