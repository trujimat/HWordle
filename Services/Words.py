def has_same_letter_at_position(word1, word2, position):
    return word1[position] == word2[position]

def does_not_have_letter(word1, word2, position):
    for letter in word2:
        if letter == word1[position]:
            return False
    return True

def has_letter_somewhere(word1, word2, position):
    if word1[position] == word2[position]:
        return False

    return any(letter == word1[position] for letter in word2)
