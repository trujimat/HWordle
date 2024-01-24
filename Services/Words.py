from Classes.Letter_Result import Letter_Result

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


def is_possible_word(chosen_word, candidate_possible_word,  letter_results):
    for i, result in enumerate(letter_results):
            if result == Letter_Result.INCORRECT:
                if not does_not_have_letter(chosen_word, candidate_possible_word, i):
                    return False
            elif result == Letter_Result.INCORRECT_PLACE:
                if not has_letter_somewhere(chosen_word, candidate_possible_word, i):
                    return False
            else:
                if not has_same_letter_at_position(chosen_word, candidate_possible_word, i):
                    return False
    return True