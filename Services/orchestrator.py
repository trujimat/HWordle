from Classes.Histogram import Histogram

def orchestrate(possible_words):

    entropy = 0
    candidate_word = ''

    for word in possible_words:
        print(f"the word in this moment is {word}")
        histogram = Histogram(possible_words = possible_words, word = word)
        histogram.create_histogram()
        histogram.compute_entropy()
        if(histogram.entropy >= entropy):
            entropy = histogram.entropy
            candidate_word = word

    return candidate_word
