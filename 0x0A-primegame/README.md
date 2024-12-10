# ALX Interview Prep

This repository contains solutions to various interview preparation problems as part of the ALX program.

## 0x0A. Prime Game

## Author
* Name: Wilfort Abel
* Email: juiciwhilf@gmail.com

### 📋 Problem Description

Maria and Ben are playing a game involving prime numbers. Given a set of consecutive integers from `1` to `n`, they take turns choosing a prime number and removing that number and its multiples from the set. 

- **Rules**:
  1. Maria always goes first.
  2. Both players play optimally.
  3. The player unable to make a move loses the game.

You are tasked with determining who the winner is after `x` rounds of the game. For each round, the input `n` may differ.

---

### 🧩 Function Prototype

```python
def isWinner(x, nums):
    """
    Determines the winner of the prime number game across multiple rounds.
    
    Args:
        x (int): Number of rounds.
        nums (list): List of integers where each integer n is the maximum number for that round.
    
    Returns:
        str: "Maria" if Maria wins the most rounds, "Ben" if Ben wins the most rounds, or None if there is no clear winner.
    """.
