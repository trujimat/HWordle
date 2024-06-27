import sys
import os

# Add the parent directory of HWordle to sys.path
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Classes.Status import Status
from Classes.Letter_Result import Letter_Result

test_words = Status()

print(test_words.possible_words)

# new_words = ['hello', 'ghost']

# test_words.update_possible_words(new_words)

# print(test_words.possible_words)

print ('--------------------------------------------------------------------------------------------------------------------------------')

test_words.chosen_word = 'hello'
test_words.letter_results[0]= Letter_Result.CORRECT
test_words.letter_results[4] = Letter_Result.CORRECT
test_words.update_possible_words()

print(test_words.possible_words)