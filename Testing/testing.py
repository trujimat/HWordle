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