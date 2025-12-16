locations = []
with open("input") as f:
    for x in f:
        locations.append(x)

width = len(locations[0])
height = len(locations)
row, col, total = 0, 0, 0

def valid_location(row, col):
    return True if row >= 0 and row < height and col >= 0 and col < width else False

def check_neighbours(row, col):
    top         = 1 if valid_location(row - 1, col) and locations[row - 1][col] == '@' else 0
    left        = 1 if valid_location(row, col - 1) and locations[row][col - 1] == '@' else 0
    right       = 1 if valid_location(row, col + 1) and locations[row][col + 1] == '@' else 0
    down        = 1 if valid_location(row + 1, col) and locations[row + 1][col] == '@' else 0

    top_left    = 1 if valid_location(row - 1, col - 1) and locations[row - 1][col - 1] == '@' else 0
    top_right   = 1 if valid_location(row - 1, col + 1) and locations[row - 1][col + 1] == '@' else 0
    down_left   = 1 if valid_location(row + 1, col - 1) and locations[row + 1][col - 1] == '@' else 0
    down_right  = 1 if valid_location(row + 1, col + 1) and locations[row + 1][col + 1] == '@' else 0
    
    return 1 if sum([top, left, right, down, top_left, top_right, down_left, down_right]) < 4 else 0

for line in locations:
    for char in line:
        if char == '@':
            total += check_neighbours(row, col)
        col += 1
    col = 0
    row += 1

print('rolls of paper accessed: ', total)
