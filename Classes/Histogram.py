import numpy as np
from itertools import product
from scipy.stats import entropy
from Classes.Possibilities import Possibilities
from Classes.Letter_Result import Letter_Result
from Services.Words import is_possible_word
from Resources.Constants import letters_per_word

class Histogram:

    def __init__(self, possible_words, word):
        self.possible_words = possible_words
        self.word = word
        self.entropy = 0
        self.histogram = [Possibilities() for _ in range(243)] 

    def create_histogram(self):
        domain = self.create_domain()
        for i in range(0, 243):
            self.histogram[i].letter_score = domain[i]
            self.histogram[i].words = self.get_possible_words(domain[i])
            self.histogram[i].length_words = len(self.histogram[i].words)
            self.histogram[i].probability = self.histogram[i].length_words/len(self.possible_words)

    def compute_entropy(self):
        probabilities = [possibility.probability for possibility in self.histogram]
        self.entropy = entropy(probabilities, base=2)

    def get_possible_words(self, index):
        # The index is a result ie: incorrect, correct, incorrect place, correct, correct
        # The flux of this function is the following for each word of possible words check if it suits the result of the index
        # If it suits append it to the result of the function

        possible_words = []

        for word in self.possible_words:
            if is_possible_word(self.word, word, index):
                possible_words.append(word)

        return possible_words


    def create_domain(self):
        # Convert Enum values to a list
        elements = [result for result in Letter_Result]

        # Generate all combinations of 5 elements
        domain = list(product(elements, repeat=letters_per_word))

        return domain
    
    def print_histogram(self):
        for entry in self.histogram:
            print(entry.letter_score)
            print(entry.words)

