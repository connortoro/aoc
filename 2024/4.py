grid = []

with open("2024/4.txt", "r") as file:
  for line in file:
    grid.append(list(line.strip()))

res = 0
n = 140 
for y in range(n):
  for x in range(n):
    if not grid[y][x] == 'X': continue

    # Across
    if x < n-3:
      s = grid[y][x] + grid[y][x+1] + grid[y][x+2] + grid[y][x+3]
      if s == "XMAS":
        res += 1

    # Backwards
    if x > 2:
      s = grid[y][x] + grid[y][x-1] + grid[y][x-2] + grid[y][x-3]
      if s == "XMAS":
        res += 1

    # Downs
    if y < n-3:
      s = grid[y][x] + grid[y+1][x] + grid[y+2][x] + grid[y+3][x]
      if s == "XMAS":
        res += 1

    # Ups
    if y > 2:
        s = grid[y][x] + grid[y-1][x] + grid[y-2][x] + grid[y-3][x]
        if s == "XMAS":
          res += 1

    # DR
    if x < n-3 and y < n-3:
      s = grid[y][x] + grid[y+1][x+1] + grid[y+2][x+2] + grid[y+3][x+3]
      if s == "XMAS":
        res += 1

    # DL
    if y < n-3 and x > 2:
      s = grid[y][x] + grid[y+1][x-1] + grid[y+2][x-2] + grid[y+3][x-3]
      if s == "XMAS":
        res += 1
    # UR
    if y > 2 and x < n-3:
      s = grid[y][x] + grid[y-1][x+1] + grid[y-2][x+2] + grid[y-3][x+3]
      if s == "XMAS":
        res += 1

    # UL
    if y > 2 and x > 2:
      s = grid[y][x] + grid[y-1][x-1] + grid[y-2][x-2] + grid[y-3][x-3]
      if s == "XMAS":
        res += 1

print(res)

res = 0
for y in range(1, n-1):
  for x in range(1, n-1):
    bs = grid[y-1][x-1] + grid[y][x] + grid[y+1][x+1]
    fs = grid[y+1][x-1] + grid[y][x] + grid[y-1][x+1]
    if (bs == "SAM" or bs == "MAS") and (fs == "SAM" or fs == "MAS"):
      res += 1

print(res)
