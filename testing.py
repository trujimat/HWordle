from Classes.Status import Status, Result

test_words = Status()

print(test_words.possible_words)

# new_words = ['hello', 'ghost']

# test_words.update_possible_words(new_words)

# print(test_words.possible_words)

print ('--------------------------------------------------------------------------------------------------------------------------------')

test_words.chosen_word = 'hello'
test_words.letter_results[0]= Result.CORRECT
test_words.letter_results[4] = Result.CORRECT
test_words.update_possible_words()

print(test_words.possible_words)