def draw_hollow_square(char_to_draw, size):
    spaces = char_to_draw - 1
    stars = 1
    size = 0
    for i in range(1, size **1):
        print(spaces)
        print(stars)
        print(spaces)
        print()
        spaces -= 1
        stars += 2
def draw_hollow_square(number):
    for i in range(number):
        print("*", end="")

def print_spaces(number):
    for i in range(number):
        print(" ", end="")

draw_hollow_square("*",5)
