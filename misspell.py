import pickle

try:
    with open('statistics.pkl', 'rb') as f:
        statistics = pickle.load(f)
except FileNotFoundError:
    statistics = {
        'misspellings': {},
        'word_occurrences': {},
    }

misspellings = statistics['misspellings']
word_occurrences = statistics['word_occurrences']

# output the misspellings sorted by frequency
print("Misspellings sorted by frequency:")
for word in sorted(misspellings, key=misspellings.get, reverse=True):
    print(f"{word}: {misspellings[word]}")
