# 0x05. N Queens: Algorithm Python

## Project Overview
The **N Queens** problem is a mathematical puzzle where the challenge is to place **N queens** on an \(N \times N\) chessboard so that no two queens threaten each other. This project employs the **backtracking algorithm**, a systematic way to explore all possible placements and find valid solutions.

---

## Table of Contents
- [Concepts Used](#concepts-used)
- [Usage](#usage)
- [Algorithm Description](#algorithm-description)
- [Resources](#resources)

---

## Concepts Used
### 1. **Backtracking Algorithms**
   - A methodical way to explore potential solutions by building them incrementally and abandoning them when they fail.
   - Example: Placing queens one row at a time and backtracking if a conflict arises.

### 2. **Recursion**
   - Used to implement backtracking by calling a function within itself until the problem is solved or deemed unsolvable.

### 3. **List Manipulation**
   - Queens' positions are stored and updated in lists during the solution process.

### 4. **Command-Line Arguments**
   - Python's `sys` module is used to pass \(N\) as an argument to specify the chessboard size.

---

## Usage
### Requirements
- **Python 3.6+** installed on your machine.
