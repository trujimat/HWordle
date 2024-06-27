import sys
import time
from Services.orchestrator import orchestrate
from Classes.Status import Status
from Classes.Letter_Result import compute_word_score

start_time = time.time() 
status = Status()

# Check if at least one argument is provided (excluding the script name)
if len(sys.argv) > 1:
    if sys.argv[1] in status.possible_words:
        answer_word = sys.argv[1]
        print(f'The answer word is {answer_word}')
    else:
        print('You have to enter a 5 letter word from file WordleWords.txt, go to README for further instructions on how to run the project')
        sys.exit(1)
else:
    print('You have to enter a 5 letter word from file WordleWords.txt, go to README for further instructions on how to run the project')
    sys.exit(1)

# Check if the second argument is provided and is a valid integer between 1 and 5
if len(sys.argv) > 2:
    try:
        num_processes = int(sys.argv[2])
        if 0 < num_processes < 6:
            print(f'The number of processes is {num_processes}')
        else:
            print('You have to enter a number of processes smaller than 6 and greater than 0, go to README for further instructions on how to run the project')
            sys.exit(1)
    except ValueError:
        print('The second argument must be an integer between 1 and 5')
        sys.exit(1)
else:
    num_processes = 1
    print(f'The number of processes is 1')

print('Running.... \n')
candidate_word = ''
iterator = 0

while iterator < 6 and candidate_word != answer_word:
    candidate_word = orchestrate(status.possible_words, num_processes)
    status.chosen_word = candidate_word
    iterator = iterator + 1
    if candidate_word != answer_word:
        status.letter_results = compute_word_score(candidate_word, answer_word)
        status.update_possible_words()

print(f'The guessed word by HWordle is {candidate_word} \n')
print(f'The word to be guessed was {answer_word} \n')
print(f'The amount of attempts taken was {iterator} \n')

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")