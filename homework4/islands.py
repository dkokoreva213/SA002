def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # помечаем посещённой
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
    return count

# Ввод данных
m = int(input("Введите количество строк m: "))
grid = []
print(f"Введите {m} строки по n символов '0' или '1' без пробелов:")
for _ in range(m):
    row = list(input().strip())
    grid.append(row)

# Вывод результата
print("Количество островов:", num_islands(grid))
