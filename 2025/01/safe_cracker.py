rotations = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

start = 50
zeroes = []

for rotation in rotations.split('\n'):
    direction, amount = rotation[0], int(rotation[1:])
    print(f"{direction = } {amount = }")
    if direction == "L":
        total = start - amount
    else:
        total = start + amount

    if total < 0:
        start = 99 - abs(total) + 1
    elif total == 100:
        start = 0
    elif total > 100:
        print("Total greater " + str(total))
        start = total - 100
    else:
        start = total

    print(f"{start = }")
    if start == 0:
        zeroes.append(start)

print(f"Total number of zeroes: {len(zeroes)}")
