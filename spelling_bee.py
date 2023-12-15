import os
import pickle
import random

# Load words from file
try:
    with open('word-list.txt', 'r') as f:
        words = [line.strip() for line in f]
except FileNotFoundError:
    raise SystemExit("Word file not found!")

# Affirmative words list
affirmative_words = [
    'Superb!',
    'Excellent!',
    'Well done!',
    'Good job!',
    'Right on!',
    'Correct!'
]

# Initialize or load statistics
try:
    with open('statistics.pkl', 'rb') as f:
        statistics = pickle.load(f)
except FileNotFoundError:
    statistics = {
        'misspellings': {},
        'word_occurrences': {},
    }

# Initialize score
score = {
    'correct': 0,
    'incorrect': 0
}

# Main spelling bee function
def spelling_bee(word):
    os.system("say " + word)
    print("Please spell the word you just heard: ")
    spelling = input()

    while spelling == "?":
        os.system("say " + word)
        print("Please spell the word you just heard: ")
        spelling = input()

    if spelling.lower() == word.lower():
        # Randomly select an affirmative word
        affirmation = random.choice(affirmative_words)
        print(affirmation)
        score['correct'] += 1
    else:
        print(f"Incorrect. The correct spelling is {word}.")
        score['incorrect'] += 1
        if word in statistics['misspellings']:
            statistics['misspellings'][word] += 1
        else:
            statistics['misspellings'][word] = 1

    if word in statistics['word_occurrences']:
        statistics['word_occurrences'][word] += 1
    else:
        statistics['word_occurrences'][word] = 1

    # Save statistics
    with open('statistics.pkl', 'wb') as f:
        pickle.dump(statistics, f)


# Get number of words from user
n = int(input("Enter a number of words for the spelling bee: "))
if n > len(words):
    n = len(words)

# Select random words
selected_words = random.sample(words, n)

# Run the spelling bee
for word in selected_words:
    spelling_bee(word)

# Print score and statistics
total = score['correct'] + score['incorrect']
print(f"Your score: {score['correct']}/{total} correct")
print(f"Misspelled words: {statistics['misspellings']}")
print(f"Word occurrences: {statistics['word_occurrences']}")

