# Rock, paper or scissors game

Rock, Paper, Scissors is a classic hand game where two players compete to choose one of three options: rock, paper, or scissors. The rules are simple: rock crushes scissors, scissors cuts paper, and paper covers rock. The game is played in rounds, with each player selecting their choice simultaneously. The winner of each round is determined based on the rules, and the first player to win two rounds is declared the overall winner. It's a fun and easy-to-learn game that can be enjoyed by people of all ages

## What i learned

-   **Functions**: The code uses functions to modularize the rock, paper, scissors game process. Functions like choose_options, check_rules, and run_game break down the code into smaller, manageable parts, making it easier to understand and maintain.

-   **User Input**: The program utilizes the input() function to prompt the user to input their choice (rock, paper, or scissors).

-   **Conditionals**: It uses conditionals (if, elif, else) to check the game rules and determine who wins each round.

-   **While Loops**: The game runs within a while True loop that stops when one player reaches two wins.

-   **Lists and Tuples**: It uses a tuple to store the valid game options (rock, paper, scissors), and a list to print the game result.

-   **Random Module**: It imports and uses the random module to have the computer randomly choose an option from the game.

-   **Logical Operators**: It uses logical operators (and, or, not) to check the game conditions, for example, if the user's option is within the valid options.

-   **Variables and Arithmetic Operations**: It uses variables to keep track of user and computer wins, and performs arithmetic operations to increment these variables based on the game result.

These are some of the Python concepts that can be learned from the provided code. Additionally, the code demonstrates how to combine these concepts to create a simple yet functional game in Python.

## Usage

To execute the game you only need to clone this project and then in your terminal run the main file --> rps-game/main.py

```sh
# clone de repo
git clone https://github.com/cristianorregodev/learning-python.git

#open the project
cd learning-python

#run rps-game
python3 rps-game/main.py
```
