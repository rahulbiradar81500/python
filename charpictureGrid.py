grid = [
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '0', '0', '0', '0', '0', '.'],
    ['.', '0', '0', '0', '0', '0', '.'],
    ['.', '.', '0', '0', '0', '0', '.'],
    ['.', '.', '.', '0', '0', '0', '.'],
    ['.', '.', '.', '.', '0', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.']
]
for row in grid:
    row_string = ''.join(row)
    print(row_string)
