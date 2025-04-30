import random
import time


CHARS = ['@', '#', '*', '+', '.']
LOGO = [
    "    ____         ",
    "   / __ \\__  __  ",
    "  / /_/ / / / /  ",
    " / ____/ /_/ /   ",
    " /_/    \\__, /   ",
    "       /____/    ",
]

def color_text(char, color_code):
    return f"\033[{color_code}m{char}\033[0m"

def generate_canvas(canvas_width, canvas_height):
    logo_height = len(LOGO)
    logo_width = len(LOGO[0])


    canvas = []
    for row in range(canvas_height):
        line = ''
        for col in range(canvas_width):
            logo_row = row % logo_height
            logo_col = col % logo_width

            if logo_col < len(LOGO[logo_row]):
                char = LOGO[logo_row][logo_col]
                if char == ' ':
                    if random.random() < 0.5:
                        line += random.choice(CHARS)  # random chars background
                    else:
                        line += ' '
                else:
                    line += color_text(char, 33)
            else:
                line += ' '
        canvas.append(line)
    return canvas

def print_canvas(canvas, delay=0.03):
    for line in canvas:
        print(line)
        time.sleep(delay)

def main():
    print(" PY Logo Tiler ")
    name = input("your work name: ")

    while True:
        try:
            width = int(input("Enter canvas width (min 30): "))
            height = int(input("Enter canvas height (min 10): "))
            if width < 30 or height < 10:
                print("Please enter values above the minimum size.")
                continue
            break
        except ValueError:
            print("❗ Please enter valid integers.")

    canvas = generate_canvas(width, height)
    print()
    print_canvas(canvas)
    print(f"\n🎉 {name}, enjoy your tiled masterpiece! 🎉")

if __name__ == "__main__":
    main()
