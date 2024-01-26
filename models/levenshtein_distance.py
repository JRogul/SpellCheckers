def levenshtein_distance(word1, word2): #Implementation based on pseudo code
    
    if len(word1) == 0:
        return len(word2)
    if len(word2) == 0:
        return len(word1)
        
    indicator = 1 if word1[0] != word2[0] else 0
    # Deletion
    levd1 = levenshtein_distance(word1[1:], word2) 
    # Insertion
    levd2 = levenshtein_distance(word1, word2[1:]) 
    # Substitution
    levd3 = levenshtein_distance(word1[1:], word2[1:]) 

    return indicator + min(levd1, levd2, levd3)
