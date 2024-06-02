import os
from Services.Words import has_same_letter_at_position, does_not_have_letter, has_letter_somewhere, is_possible_word
from Classes.Letter_Result import Letter_Result
from Resources.Constants import letters_per_word

class Status:

    def __init__(self):
        self.chosen_word = ''
        self.possible_words = set(self.obtain_initial_word_list())
        self.letter_results = [Letter_Result.INCORRECT] * letters_per_word

    def obtain_initial_word_list(self):
        path = os.path.abspath(__file__)
        resources_dir = os.path.join(os.path.dirname(path), '..', 'Resources')
        file_path = os.path.join(resources_dir, 'WordleWordsTest.txt')

        with open(file_path, 'r') as file:
            lines = file.readlines()

        return [line.strip() for line in lines]

    def update_possible_words(self):
        if not self.found_word():
            self.possible_words = {word for word in self.possible_words if is_possible_word(self.chosen_word, word, self.letter_results)}
            self.possible_words.discard(self.chosen_word)
    
    def found_word(self):
        return all(result == Letter_Result.CORRECT for result in self.letter_results)