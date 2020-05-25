#!/usr/bin/python3
""" Give probabilities to move the queen in chess """
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    moves = []

    for i in range(n):
        moves.append([i, None])

    def checks_queen(num):
        for i in range(n):
            if num == moves[i][1]:
                return True
        return False

    def reject(word, num):
        if checks_queen(num):
            return False
        i = 0
        while i < word:
            if abs(moves[i][1] - num) == abs(i - word):
                return False
            i += 1
        return True

    def clear_moves(word):
        for i in range(word, n):
            moves[i][1] = None

    def backtracking(word):
        for num in range(n):
            clear_moves(word)
            if reject(word, num):
                moves[word][1] = num
                if (word == n - 1):
                    print(moves)
                else:
                    backtracking(word + 1)

    backtracking(0)
