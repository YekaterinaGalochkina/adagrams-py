from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    letters = []
    for key, value in LETTER_POOL.items():
        for _ in range(value):
            letters.append(key)
    hand = []
    for _ in range(10):
        index = randint(0, len(letters) - 1)
        letter = letters.pop(index)
        hand.append(letter)
    return hand

def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    for letter in word:
        if letter.upper() not in letter_bank_copy:
            return False
        letter_bank_copy.remove(letter.upper())
    return True

def score_word(word):
    pass


def get_highest_word_score(word_list):
    pass
