---

# **Tic Tac Toe Game**

A simple command-line implementation of the classic Tic Tac Toe game for two players. Players take turns marking spaces on a 3x3 grid, aiming to form a winning combination.

---

## **Features**

- Classic Tic Tac Toe gameplay.
- Supports two players: "X" and "O".
- Checks for winning combinations after every move.
- Detects game outcomes (Win or Draw).
- Option to quit mid-game.

---

## **Installation**

### **Prerequisites**
- Python 3.x installed on your system.

### **Steps**
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/tic-tac-toe.git
   ```
2. Navigate to the project directory:
   ```bash
   cd tic-tac-toe
   ```
3. Run the game:
   ```bash
   python main.py
   ```

---

## **Usage**

1. Launch the game by running the script.
2. The game begins with Player X.
3. Players take turns entering a number (1-9) to mark their move on the grid:
   - `1` to `9` corresponds to positions on the board:
     ```plaintext
      1 | 2 | 3
     -----------
      4 | 5 | 6
     -----------
      7 | 8 | 9
     ```
4. The game announces the winner when a player forms a winning combination or ends in a draw if the board is full.
5. To exit mid-game, type `e`.

---

## **Winning Combinations**

A player wins by marking any of these combinations:
- Diagonal: 1-5-9, 3-5-7
- Horizontal: 1-2-3, 4-5-6, 7-8-9
- Vertical: 1-4-7, 2-5-8, 3-6-9

---

## **Technologies Used**

- **Python**: Core programming language.

---

## **Acknowledgments**

- Inspired by the classic Tic Tac Toe game.
- ASCII art and simple design make it fun and easy to play in a terminal.

---
