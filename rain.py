import colorama
import os
import time
import sys
import random

def printAt(x, y, text):
	print("\033[" + str(x) + ";" + str(y) + "H" + text, end="")
def deleteAt(x, y):
    print("\033[" + str(x) + ";" + str(y) + "H\r\x1b[K", end="")

colorama.init()
os.system("cls")
CMD_WIDTH = os.get_terminal_size()[0]
CMD_HEIGHT = os.get_terminal_size()[1]

rand_col_nums = random.sample(range(0, CMD_WIDTH + 1), 30)
columns = []
for i in rand_col_nums:
    rand_row_nums = random.sample(range(0, CMD_HEIGHT), 3)
    column = [[x, i] for x in rand_row_nums]
    columns.append(column)

while True:
    for column in columns:
        for pos in column:
            printAt(pos[0], pos[1], "|")
    time.sleep(0.01)
    for column in columns:
        for pos in column:
            deleteAt(pos[0], pos[1])
    for column in columns:
        for pos in column:
            pos[0] += 1
            if pos[0] >= CMD_HEIGHT:
                pos[0] = random.randint(0, CMD_HEIGHT // 3)