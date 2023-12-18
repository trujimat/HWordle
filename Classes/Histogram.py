import numpy as np
from scipy.stats import entropy
from Classes.Possibilities import Possibilities

class Histogram:

    def __init__(self, possible_words, word):
        self.possible_words = possible_words
        self.word = word
        self.entropy = 0
        self.histogram = [Possibilities()]*125
        

    def compute_entropy(self):
        probabilities = [possibility['probability'] for possibility in self.histogram]
        self.entropy = entropy(probabilities, base=2)

    def create_histogram(self):
        for i in range(0, 125):
            # self.histogram[i].letter_score = 
            self.histogram[i].words = self.get_possible_words(i)
            self.histogram[i].length_words = len(self.histogram[i].words)
            self.histogram[i].probability = self.histogram[i].length_words/len(self.possible_words)

    def get_possible_words(self, index):
        # The index is a result ie: incorrect, correct, incorrect place, correct, correct
        # The flux of this function is the following for each word of possible words check if it suits the result of the index
        # If it suits append it to the result of the function

        # possible_words = []

        # for word in self.possible_words:
        #     is_possible_word = is_possible_word(word, index)
        #     if is_possible_word:
        #         possible_words.append(word)

        pass

