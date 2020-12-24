# Grid : tableau de 9 sur 9
def solve(grid):
  if isGridComplete(grid):
    return True
  for i in range(9):
    for j in range(9):
      if grid[i][j] == 0:
        for valueToTest in range (1, 10):
          # Si on peut marquer la case courante avec le nombre courant (ie la grille est valide),
          # on marque la case et on regarde si la grille est résolvable
          # avec cette nouvelle version de la grille, si elle n'est pas résolvable
          # on fait machine arrière (backtracking) et on remet la case à 0
          isValidMove = isValid(grid, i, j, valueToTest)
          if (isValidMove):
            grid[i][j] = valueToTest
            if solve(grid):
              return True
        # Si on atteint cette instruction cela signifie qu'il n'y a aucune valeur possible permettant de résoudre la grille
        grid[i][j] = 0
        return False
  return False

def isGridComplete(grid):
  for i in range(9):
    for j in range(9):
      if grid[i][j] == 0:
        return False
  return True

def isValid(grid, i, j, valueToTest):
  # Check row
  for colIndex in range(len(grid[i])):
    if grid[i][colIndex] == valueToTest:
      return False
    
  # Check column
  for rowIndex in range(len(grid[j])):
    if grid[rowIndex][j] == valueToTest:
      return False

  # Check Box
  box_x = i // 3
  box_y = j // 3
  for rowIndex in range(box_x * 3, box_x * 3 + 3):
    for colIndex in range(box_y * 3, box_y * 3 + 3):
      if grid[rowIndex][colIndex] == valueToTest:
        return False
  return True