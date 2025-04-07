def print_right(text):
    length = len(text)
    space_printing_length = 40 - length
    print(" " * space_printing_length + text)
    return length

print_right("hi")

def triangle(letter, ocurrance):
    for i in range(ocurrance):
        print(letter * (i + 1))
    return
triangle("a", 5)

def rectangle(letter, rows, columns):
    for i in range(rows):
        print(letter * columns)
    return
rectangle("b", 3, 5)


def bottle_verse(n):
    for i in range(n, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down and pass it around, {i - 1} bottles of beer on the wall.")
        elif i == 1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print(f"Take one down and pass it around, no more bottles of beer on the wall.")
        else:
            print("No more bottles of beer on the wall, no more bottles of beer.")
            print("Go to the store and buy some more, 99 bottles of beer on the wall.")
bottle_verse(5)

