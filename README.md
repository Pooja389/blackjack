# Blackjack Game

This is a simple console-based Blackjack game implemented in Python. The game allows a user to play against the computer using standard Blackjack rules.

## Features

- Allows the player to choose if they want to play or exit.
- Randomly generates cards for the player and the computer.
- The player can choose to take additional cards until they decide to stop or exceed a total of 21 points.
- The computer takes cards automatically until its total is 17 or more.
- Determines the winner based on the Blackjack rules.

## How It Works

1. The game starts by asking if the user wants to play Blackjack (`'yes'` or `'no'`).
2. If the user chooses `'yes'`:
   - The player receives two initial cards, and the computer receives one.
   - The player can choose to take additional cards or stop.
   - The computer will continue taking cards until its total reaches 17 or more.
3. The winner is determined as follows:
   - If both the player and the computer exceed 21 points, the game is a draw.
   - If the player exceeds 21 points, the computer wins.
   - If the computer exceeds 21 points, the player wins.
   - If neither exceeds 21 points, the one with the higher total wins.

4. If the user chooses `'no'`, the game ends.

## Installation

1. Clone the repository or download the `blackjack.py` file.
2. Make sure you have Python installed on your system.

## Usage

1. Run the `blackjack.py` file:
   ```bash
   python blackjack.py
