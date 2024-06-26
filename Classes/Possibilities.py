from Classes.Letter_Result import Letter_Result
from Resources.Constants import letters_per_word

class Possibilities:

    def __init__(self, letter_score=[Letter_Result.INCORRECT] * letters_per_word, words='', length_words=0, probability=0):
        self.letter_score = letter_score
        self.words = words
        self.length_words = length_words
        self.probability = probability