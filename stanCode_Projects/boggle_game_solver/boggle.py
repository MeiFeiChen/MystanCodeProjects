"""
File: boggle.py
Name: Mei-Fei Chen
----------------------------------------
to play a boggle game on a 4 x4 board.Each square of the board contains a letter.
The program can find all the words, where a word can be formed using adjacent (up, down, left, right,
and diagonal) letters. No letter can be used more than once.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
SIZE = 4


class TriNode:
    def __init__(self):
        self.children = {}
        self.end = False


def main():
    """
    TODO: to play a boggle game on a 4 x4 board
    """
    # create 4x4 board
    board = []
    while len(board) < SIZE:
        row = input(f'{len(board) + 1} row of letters: ').lower().split()  # case-insensitive
        if len(row) == SIZE:
            for i in row:
                # 在同一格輸入長度多於1的字元或字元不是英文字 -> Illegal input
                if len(i) != 1 or not i.isalpha():
                    print('Illegal input')
                    break
            else:
                board.append(row)
        else:
            print('Illegal input')

    start = time.time()

    # read dictionary
    trie = read_dictionary()

    # boggle
    boggle(board, trie)

    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(board, trie):
    word_list = []
    for x in range(SIZE):
        for y in range(SIZE):
            boggle_helper(board, '', x, y, word_list, trie)
    print(f'There are {len(word_list)} words in total.')


def boggle_helper(board, string, x, y, word_list, trie):
    """
    :param board: list, list of 4x4 board
    :param string: str, letters made up by adjacent letters
    :param x: int, x position
    :param y: int, y position
    :param word_list: list, list of the words found in dictionary
    :param trie: (TriNode) a tree data structure used to store and retrieve keys in words of the dictionary
    """
    # choose
    letter = board[x][y]
    board[x][y] = ''
    string += letter

    if has_prefix(string, trie)[0]:

        # base case
        if len(string) >= SIZE:
            if has_prefix(string, trie)[1]:
                if string not in word_list:
                    word_list.append(string)
                    print(f'Found "{string}"')

        # recursive case
        # find adjacent letters
        x_y_list = [(i, j) for i in range(x - 1, x + 2) if 0 <= i < SIZE
                    for j in range(y - 1, y + 2) if 0 <= j < SIZE if i != x or j != y]
        for new_x, new_y in x_y_list:
            if board[new_x][new_y]:
                boggle_helper(board, string, new_x, new_y, word_list, trie)

    # un-choose
    board[x][y] = letter


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    :return: (TriNode) a tree data structure used to store and retrieve keys in words of the dictionary
    """
    trie = TriNode()
    with open(FILE, 'r') as f:
        for raw in f:
            word = raw.strip()
            cur = trie
            for ch in word:
                if ch in cur.children:
                    cur = cur.children[ch]
                else:
                    cur.children[ch] = TriNode()
                    cur = cur.children[ch]
            cur.end = True

    return trie


def has_prefix(sub_s, trie):
    """
    :param trie: (TriNode) a tree data structure used to store and retrieve keys in words of the dictionary
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool, bool) If there is any word with prefix stored in sub_s, if there is any word == prefix
    """
    cur = trie
    for ch in sub_s:
        if ch in cur.children:
            cur = cur.children[ch]
        else:
            return False, cur.end
    return True, cur.end


if __name__ == '__main__':
    main()
