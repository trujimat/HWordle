import sys
import time
from Services.orchestrator import orchestrate
from Classes.Status import Status
from Classes.Letter_Result import compute_word_score

start_time = time.time() 

answer_word = sys.argv[1]
print(f'the answer word is {answer_word}')
num_processes = int(sys.argv[2])
print(f'the number of processes is {num_processes}')
candidate_word = ''
iterator = 0
status = Status()

while iterator < 6 and candidate_word != answer_word:
    print(f"the value of iterator is {iterator}")
    candidate_word = orchestrate(status.possible_words, num_processes)
    print(f"the orchestrated word is {candidate_word}")
    status.chosen_word = candidate_word
    iterator = iterator + 1
    if candidate_word != answer_word:
        status.letter_results = compute_word_score(candidate_word, answer_word)
        status.update_possible_words()

print('Lets check if we got the word \n')
print(f'The last candidate word is {candidate_word}')

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")

# I don't commit anything I haven't tested!!!
