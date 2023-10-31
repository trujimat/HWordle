import os
from Services.Words import has_same_letter_at_position, does_not_have_letter, has_letter_somewhere
from Classes.Letter_Result import Letter_Result

class Status:

    def __init__(self):
        self.chosen_word = ''
        self.possible_words = set(self.obtain_initial_word_list())
        self.letter_results = [Letter_Result.INCORRECT] * 5

    def obtain_initial_word_list(self):
        path = os.path.abspath(__file__)
        resources_dir = os.path.join(os.path.dirname(path), '..', 'Resources')
        file_path = os.path.join(resources_dir, 'WordleWords.txt')

        with open(file_path, 'r') as file:
            lines = file.readlines()

        return [line.strip() for line in lines]

    def update_possible_words(self):
        if not self.found_word():
            self.possible_words = {word for word in self.possible_words if self.is_possible_word(word)}
            self.possible_words.discard(self.chosen_word)

    def is_possible_word(self, word):
        for i, result in enumerate(self.letter_results):
            if result == Letter_Result.INCORRECT:
                if not does_not_have_letter(self.chosen_word, word, i):
                    return False
            elif result == Letter_Result.INCORRECT_PLACE:
                if not has_letter_somewhere(self.chosen_word, word, i):
                    return False
            else:
                if not has_same_letter_at_position(self.chosen_word, word, i):
                    return False
        return True
    
    def found_word(self):
        return all(result == Letter_Result.CORRECT for result in self.letter_results)