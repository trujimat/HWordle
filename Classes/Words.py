import os

class Words:

    def __init__(self) -> None:
        possible_words = self.obtain_initial_word_list()

    def obtain_initial_word_list():
        resources_dir = os.path.join(os.path.dirname(__file__), 'Resources')
        file_path = os.path.join(resources_dir, 'Wordle Words.txt')

        with open(file_path, 'r') as file:
            lines = file.readlines()

        word_list = []

        for line in lines:
            word = line.strip()
            word_list.append(word)

        return word_list
    
    def update_possible_words(chosen_word, score):
        pass