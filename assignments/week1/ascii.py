import random
import time

chars = ['@', '#', '$', '%', '*', '+', '-', '=', '.']

width = 50
height = 10
row_start=2
col_start=15

logo = [
    "    ____         ",
    "   / __ \\__  __  ",
    "  / /_/ / / / /  ",
    " / ____/ /_/ /   ",
    " /_/    \\__, /   ",
    "       /____/    ",
]

print('\n')
for row in range(height):
    line = ''
    for col in range(width):
        logo_row = row - row_start
        if 0 <= logo_row < len(logo):
            logo_line = logo[logo_row]
            logo_col = col - col_start
            if 0 <= logo_col < len(logo_line):
                line += logo_line[logo_col]
                continue
        line += random.choice(chars)
    print(line)
