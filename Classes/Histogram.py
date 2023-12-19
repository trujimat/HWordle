import numpy as np
from itertools import product
from scipy.stats import entropy
from Classes.Possibilities import Possibilities
from Classes.Letter_Result import Letter_Result

class Histogram:

    def __init__(self, possible_words, word):
        self.possible_words = possible_words
        self.word = word
        self.entropy = 0
        self.histogram = [Possibilities()]*243
        

    def compute_entropy(self):
        probabilities = [possibility['probability'] for possibility in self.histogram]
        self.entropy = entropy(probabilities, base=2)

    def create_histogram(self):
        domain = self.create_domain()
        for i in range(0, 243):
            self.histogram[i].letter_score = domain[i]
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

    def create_domain(self):
        # Convert Enum values to a list
        elements = [result.value for result in Letter_Result]

        # Generate all combinations of 5 elements
        domain = list(product(elements, repeat=5))

        return domain

