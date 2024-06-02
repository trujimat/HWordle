from enum import Enum
from Resources.Constants import letters_per_word

class Letter_Result(Enum):
    CORRECT = 'CORRECT'
    INCORRECT = 'INCORRECT'
    INCORRECT_PLACE = 'INCORRECT PLACE'

def compute_word_score(chosen_word, answer_word):
    # This function will initially be just for testing
    word_result = [Letter_Result.INCORRECT] * letters_per_word

    for i in range(0, letters_per_word):
        if chosen_word[i] == answer_word[i]:
            word_result[i] = Letter_Result.CORRECT
        elif chosen_word[i] in answer_word:
            word_result[i] = Letter_Result.INCORRECT_PLACE
        else:
            word_result[i] = Letter_Result.INCORRECT

    return word_result
        