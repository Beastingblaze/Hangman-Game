# 🎮 Hangman Game (Python)

A feature-rich **Hangman Game** built with Python, using word–hint pairs, ASCII hangman art, automatic letter reveals, and clean modular design. The game reads words from a file, provides hints, and reveals a portion of letters at the start for a better experience.

---

## ⭐ Features

### 🔤 Word & Hint System

* Words and hints are loaded from `words.txt`

* Validates formatting (`word:hint`)
* Errors shown for missing or incorrect files

### 🎭 Hangman ASCII Art

* Dynamic visual hangman stages


### 🧠 Smart Gameplay Enhancements

* Reveals a percentage of random letters at game start

* Hint appears after configurable wrong attempts
* Tracks guessed letters and remaining attempts

### 🧩 Modular Code Structure

* `main.py` starts the game

* `utils.py` handles file loading & display functions

* `hangman.py` contains full game logic


---

## 📁 Project Structure

```
.
├── main.py
├── hangman.py
├── utils.py
├── words.txt
└── README.md
```

---

## 🚀 How to Run

### 1️⃣ Make sure you have Python 3 installed

Check using:

```bash
python --version
```

### 2️⃣ Run the game

```bash
python main.py
```

---

## 📝 Word File Format

Your `words.txt` file should contain entries in this format:

```
word: hint
```

Example:


```
apple: a fruit
dog: an animal
piano: a musical instrument
```

---

## 🔍 How the Game Works

### At Game Start:

* A random word and its hint are selected
* A portion of letters are auto-revealed

* Game informs the player about revealed letters

### During Play:

* Player guesses one letter at a time
* Hangman art updates for each wrong guess
* Hints appear automatically once wrong guesses reach the threshold


### Win/Lose Conditions:

* **Win:** All letters guessed
* **Lose:** No attempts left — final art displayed

---

## 🧪 Error Handling

The game gracefully handles:

* Missing `words.txt`
* Wrong formatting (`word:hint`)
* Repeated guesses
* Invalid guesses (non-letter input)

Code referencing examples:



---

## 💡 Future Improvements (Optional Ideas)

* GUI version using Tkinter
* Score tracking system
* Difficulty levels
* Multiplayer mode

---

## 📜 License

This project is open-source and free for educational or personal use.

---
