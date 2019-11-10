#!/usr/bin/env python
import sys

# from PIL import Image

def import_color(filename, y):
    im = Image.open(filename)
    print(f"{im.format}, {im.size}, {im.mode}") # => JPEG, (2998, 2277), RGB
    width, height = im.size

    # 101 pixels down is our row to pull, ie (0,101) to (2297,101)
    for x in range(width):
        try:
            pixel_color = im.getpixel((x, y))
        except IndexError as e:
            print(f"IndexError for {x}, {y}: {e}")
            break

    # 1550,1170 is roughly the center. Want to go up-right from there
    x_min = 1550
    x_max = 1550 + 1170     # since we go diagonally up-right
    y_min = 0
    y_max = 1170
    for y in range(0, y_max):   # so moving down/left
        x = x_min + 1170 - y
        pixel_color = im.getpixel((x, y))
        print(f'<div class="test-area" style="background-color:RGB{pixel_color}" onclick="console.log(\'{pixel_color}\');"></div> <!-- {x},{y} -->')

def import_chosen_colors():
    with open("./chosencolors.txt") as infile:
        for line in infile:
            line = line.replace('\n', '')
            print(f'<div class="test-area" style="background-color:RGB{line}"></div>')

def reverseprint():
    printed = False
    with open("./chosen2.txt") as infile:
        stack = []
        for line in infile:
            line = line.replace('\n', '')
            if not stack:
                print(f"first {line}")
            stack.append(line)
        while stack:
            line = stack.pop()
            print(line)


def colors_to_hex():
    import re
    with open('./chosencolors.txt') as infile:
        for line in infile:
            line = line.replace(' ', '')
            m = re.search('([0-9]+),([0-9]+),([0-9]+)', line)
            r = int(m.group(1))
            g = int(m.group(2))
            b = int(m.group(3))
            print("'#%02x%02x%02x'," % (r, g, b))

if __name__ == "__main__":
    filename = "./IMG_9538.jpg"
    # y = 1163
    # import_color(filename, 0)

    # import_chosen_colors()
    # reverseprint()

    colors_to_hex()
