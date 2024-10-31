# TODO: Ask the user for how many rows.
rows = int(input("How many rows would you like?"))
# And store it in a variable call rows.

for row in range(1, rows + 1):
    for star in range(1, row + 1):
        print("* ", end="")
    print()