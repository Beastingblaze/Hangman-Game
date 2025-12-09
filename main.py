from hangman import HangmanGame
from utils import load_words_from_file

def main():
    try:
        word_list = load_words_from_file("words.txt")
        game = HangmanGame(word_list, hint_threshold=2, reveal_percentage=0.35)
        game.play()
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        print("Please ensure 'words.txt' exists and contains valid 'word:hint' lines.")

if __name__ == "__main__":
    main()