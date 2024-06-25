import multiprocessing
import time
from Classes.Histogram import Histogram

def orchestrate(possible_words, num_processes):

    with multiprocessing.Manager() as manager:
        shared_data = manager.dict()
        lock = manager.Lock()
        
        # Adjust the number of processes based on the number of possible words
        num_words = len(possible_words)
        num_processes = min(num_processes, num_words)

        # Initialize shared data
        for i in range(num_processes):
            shared_data[f'entropy_{i}'] = 0
            shared_data[f'candidate_word_{i}'] = ''

        # Split the possible words into `num_processes` parts
        possible_words_parts = list(split_set_by_parts(possible_words, num_processes))

        # Create and start processes
        processes = []
        for i in range(num_processes):
            p = multiprocessing.Process(target=orchestrate_subprocess, args=(possible_words_parts[i], shared_data, lock, i))
            processes.append(p)
            p.start()

        # Print process IDs
        for i, p in enumerate(processes):
            print(f"ID of process p{i+1}: {p.pid}")

        # Wait until all processes are finished
        for p in processes:
            p.join()

        # Determine the final candidate word with the highest entropy
        max_entropy_index = max(range(num_processes), key=lambda i: shared_data[f'entropy_{i}'])
        candidate_word_final = shared_data[f'candidate_word_{max_entropy_index}']

        return candidate_word_final

def orchestrate_subprocess(possible_words, shared_data, lock, index):

    for word in possible_words:
        print(f"The word in this moment is {word}")
        histogram = Histogram(possible_words=possible_words, word=word)
        histogram.create_histogram()
        histogram.compute_entropy()

        with lock:
            if histogram.entropy >= shared_data[f'entropy_{index}']:
                shared_data[f'entropy_{index}'] = histogram.entropy
                shared_data[f'candidate_word_{index}'] = word

def split_set_by_parts(input_set, num_parts):
    input_list = list(input_set)
    part_size = len(input_list) // num_parts
    remainder = len(input_list) % num_parts

    parts = []
    start = 0
    for i in range(num_parts):
        end = start + part_size + (1 if i < remainder else 0)
        parts.append(input_list[start:end])
        start = end

    return parts

