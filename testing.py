from Classes.Status import Status

test_words = Status()

print(test_words.possible_words)

new_words = ['hello', 'ghost']

test_words.update_possible_words(new_words)

print(test_words.possible_words)