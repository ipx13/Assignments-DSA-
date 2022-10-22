'''
Date created: 22/10/22
Author: Paniza, Irish | BSCOE 2-2
Submitted to Mr. Madrigalejos for CMPE 30052
'''

# Letters
letter_I = [[' ' for i in range(5)] for j in range(5)]
letter_H = [[' ' for x in range(5)] for y in range(5)]
letter_R = [[' ' for a in range(5)] for b in range(5)]
letter_S = [[' ' for m in range(5)] for n in range(5)]

# Letter I
for row in range(5):
    for col in range(5):
        if (row == 0 or row == 4) or (col == 2):
            letter_I[row][col] = '#'
# Letter H
for row in range(5):
    for col in range(5):
        if (row == 2) or (col == 0 or col == 4):
            letter_H[row][col] = '#'
# Letter R
for row in range(5):
    for col in range(5):
        if ((row == 0 or row == 2) and col != 4) or (col == 0 or (row != 0 and row != 2 and col == 4)):
            letter_R[row][col] = '#'
# Letter S
for row in range(5):
    for col in range(5):
        if (row == 0 and col != 0) or (row == 1 and col == 0) or (row == 2 and (col != 0 and col != 4)) or (row == 3 and col == 4) or (row == 4 and col != 4):
            letter_S[row][col] = "#"

# Display
for i in range(5):
    for j in range(5):
        print(letter_I[i][j], end="")
    print(end="  ")
    for j in range(5):
        print(letter_R[i][j], end="")
    print(end="  ")
    for j in range(5):
        print(letter_I[i][j], end="")
    print(end="  ")
    for j in range(5):
        print(letter_S[i][j], end="")
    print(end="  ")
    for j in range(5):
        print(letter_H[i][j], end="")
    print()