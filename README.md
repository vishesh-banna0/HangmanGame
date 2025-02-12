# HangmanGame

A command-line Hangman game implemented in Python, where players guess a randomly selected word within a limited number of attempts.

## Features
- Random word selection from a predefined list (stored in `input.json`).
- 10 lives per game, with each incorrect guess reducing one life.
- Hints provided at specific life thresholds (7, 4, and 1 lives left).
- Displays the current progress of guessed letters.
- Handles incorrect guesses and provides feedback.
- Winning and losing conditions.

## Installation
### Prerequisites
Ensure you have Python installed (>=3.x).

### Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/vishesh-banna0/HangmanGame.git
   ```
2. Navigate to the project directory:
   ```sh
   cd HangmanGame
   ```
3. Run the game:
   ```sh
   python main.py
   ```

## File Structure
```
HangmanGame/
├── main.py        # Main game logic
├── input.json     # JSON file containing words and hints
├── README.md      # Project documentation
```

## How to Play
1. The game randomly selects a word, and you have 10 lives.
2. Enter one letter at a time to guess the word.
3. Each incorrect guess reduces your lives by 1.
4. Hints appear automatically when you reach 7, 4, or 1 lives.
5. Guess all letters correctly to win, or lose when lives reach 0.

## Example Gameplay
```
Welcome!! to the Hangman Game.
Here are Rules.
1. I have chosen a word you have 10 lives.
2. You have to guess the word.
3. Every wrong guess will decrease your life by 1.
4. After every three continuous fails, a hint will be provided.

Enter Your Guess: a
Incorrect Guess
Lives Left: 9
HINT: None

Enter Your Guess: e
You guessed correct

Enter Your Guess: p
Incorrect Guess
Lives Left: 7
HINT: A large land animal.
```

## Contributing
Feel free to fork the repository and submit pull requests for improvements.

## License
This project is open-source and available under the MIT License.

---

Happy Coding! 🎉

