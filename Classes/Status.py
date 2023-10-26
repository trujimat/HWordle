import os
from enum import Enum

class Result(Enum):
    CORRECT = 'CORRECT'
    INCORRECT = 'INCORRECT'
    INCORRECT_PLACE = 'INCORRECT PLACE'

class Status:

    def __init__(self) -> None:
        self.chosen_word = ''
        self.possible_words = self.obtain_initial_word_list()
        self.first_letter = Result.INCORRECT
        self.second_letter = Result.INCORRECT
        self.third_letter = Result.INCORRECT
        self.fourth_letter = Result.INCORRECT
        self.fifth_letter = Result.INCORRECT

    def obtain_initial_word_list(self):

        path = os.path.abspath(__file__)
        resources_dir = os.path.join(os.path.dirname(path), '..', 'Resources')
        file_path = os.path.join(resources_dir, 'WordleWords.txt')

        with open(file_path, 'r') as file:
            lines = file.readlines()

        word_list = []

        for line in lines:
            word = line.strip()
            word_list.append(word)

        return word_list
    
    def update_possible_words(self, possible_words):
        self.possible_words = possible_words

    def discard_words(self):

        updated_possible_words = []        
        for word in self.possible_words:
            if self.is_possible_word(word):
                updated_possible_words.append(word)

        return updated_possible_words
