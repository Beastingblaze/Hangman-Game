import os

def load_words_from_file(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Word file '{filename}' not found.")
    
    words_and_hints = []
    with open(filename, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            if ':' not in line:
                raise ValueError(f"Invalid format on line {line_num}: '{line}'. Expected 'word:hint'.")
            parts = line.split(':', 1)
            if len(parts) != 2 or not parts[0].strip() or not parts[1].strip():
                raise ValueError(f"Invalid format on line {line_num}: '{line}'. Word and hint must be non-empty.")
            word = parts[0].strip().lower()
            hint = parts[1].strip()
            words_and_hints.append((word, hint))
    
    if not words_and_hints:
        raise ValueError(f"No valid word:hint pairs found in '{filename}'.")
    
    return words_and_hints

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def display_hangman(attempts_left):
    stages = [
        r"""
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        """,
        r"""
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        """,
        r"""
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========
        """,
        r"""
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        r"""
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        r"""
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        r"""
           +---+
           |   |
               |
               |
               |
               |
        =========
        """
    ]
    return stages[attempts_left]      