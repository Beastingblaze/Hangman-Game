
import random
import math
from utils import load_words_from_file, display_word, display_hangman

class HangmanGame:
    def __init__(self, word_list, max_attempts=6, hint_threshold=0, reveal_percentage=0.25):
        self.word, self.hint = random.choice(word_list)
        self.guessed_letters = set()
        self.max_attempts = max_attempts
        self.attempts_left = max_attempts
        self.hint_threshold = hint_threshold
        self.wrong_guesses = 0
        
        unique_letters = set(self.word)
        num_to_reveal = max(1, math.floor(len(unique_letters) * reveal_percentage))
        revealed_letters = random.sample(list(unique_letters), min(num_to_reveal, len(unique_letters)))
        self.guessed_letters.update(revealed_letters)
    
    def guess_letter(self, letter):
        letter = letter.lower()
        if len(letter) != 1 or not letter.isalpha():
            raise ValueError("Guess must be a single letter.")
        if letter in self.guessed_letters:
            raise ValueError("Letter already guessed.")
        
        self.guessed_letters.add(letter)
        if letter in self.word:
            return True
        else:
            self.attempts_left -= 1
            self.wrong_guesses += 1
            return False
    
    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)
    
    def is_lost(self):
        return self.attempts_left <= 0
    
    def get_display_word(self):
        return display_word(self.word, self.guessed_letters)
    
    def get_hangman_art(self):
        return display_hangman(self.attempts_left)
    
    def should_show_hint(self):
        return self.wrong_guesses >= self.hint_threshold
    
    def play(self):
        print("Welcome to Hangman with Hints and Reveals!")
        print(f"The word has {len(self.word)} letters.")
        print(f"Revealed letters: {', '.join(sorted(self.guessed_letters))}")
        if self.hint_threshold == 0:
            print(f"Hint: {self.hint}")
        
        while not self.is_won() and not self.is_lost():
            print(self.get_hangman_art())
            print(f"Word: {self.get_display_word()}")
            print(f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")
            print(f"Attempts left: {self.attempts_left}")
            
            if self.should_show_hint() and self.hint_threshold > 0:
                print(f"Hint: {self.hint}")
            
            try:
                guess = input("Guess a letter: ").strip()
                is_correct = self.guess_letter(guess)
                if is_correct:
                    print("Good guess!")
                else:
                    print("Wrong guess!")
            except ValueError as e:
                print(f"Error: {e}")
        
        if self.is_won():
            print(f"Congratulations! You guessed the word: {self.word}")
        else:
            print(self.get_hangman_art())
            print(f"Game over! The word was: {self.word}")