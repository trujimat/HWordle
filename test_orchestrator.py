from orchestrator import orchestrate
from Classes.Status import Status
from Classes.Letter_Result import Letter_Result, compute_word_score

answer_word = 'amber'
candidate_word = ''
iterator = 0
status = Status()

while iterator < 6 and candidate_word != answer_word:
    print(f"the value of iterator is {iterator}")
    candidate_word = orchestrate(status.possible_words)
    print(f"the orchestrated word is {candidate_word}")
    status.chosen_word = candidate_word
    iterator = iterator + 1
    if candidate_word != answer_word:
        status.letter_results = compute_word_score(candidate_word, answer_word)
        status.update_possible_words()

print('Lets check if we got the word \n')
print(f'The last candidate word is {candidate_word}')


# I don't commit anything I haven't tested!!!
