from Classes.Histogram import Histogram
from Classes.Letter_Result import Letter_Result
from Classes.Status import Status

test_words = Status()

test_histogram = Histogram(possible_words=test_words.possible_words, word='hello')
test_histogram.possible_words = test_words.possible_words

print ('the possible words are')
print (test_histogram.possible_words)

print ('--------------------------------------------------------------------------------------------------------------------------------')

test_histogram.create_histogram()
test_histogram.compute_entropy()

print('lets check the histogram')
print ('--------------------------------------------------------------------------------------------------------------------------------')
test_histogram.print_histogram()
print(f'the entropy is {test_histogram.entropy}')
print ('-----------------------------------------------Finished testing--------------------------------------------------------------')