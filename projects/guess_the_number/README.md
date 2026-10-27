# Guess the Number — Python OOP Game

## About
A command-line number guessing game built with Python. This project is part of my daily programming practice and demonstrates object-oriented programming and problem-solving.

## Features
- Three difficulty levels: Easy, Medium, and Hard
- Random number generation
- Maximum of 7 valid guesses
- Feedback when the guess is too high or too low
- Input validation
- Tracks the number of attempts
- Reveals the secret number when the player loses

## Difficulty Levels
| Level | Number Range |
|---|---|
| Easy | 1–50 |
| Medium | 1–100 |
| Hard | 1–500 |

## Concepts Practiced
- Classes and objects
- Constructors (`__init__`)
- Instance attributes and methods
- Conditional statements
- `while` loops
- Exception handling with `try/except`
- The `random` module
- Functions and the `main()` entry point

## How to Run
Make sure Python 3 is installed.

```bash
python guess_the_number.py
```

## How to Play
1. Choose a difficulty level.
2. Enter an integer within the displayed range.
3. Follow the hints to find the secret number.
4. Guess correctly within 7 valid attempts to win.

## Future Improvements
- Add a replay option.
- Save the best score.
- Add automated tests.
