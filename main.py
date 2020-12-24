from sudoku import solve
import json

with open('grid.json', 'r') as json_file:
  data = json.load(json_file)
  grid = data['grid']
  solved_grid = grid.copy()
  print("Starting to solve the grid")
  solve(solved_grid)
  data['solution'] = solved_grid
  print(f"Finished to solve the grid")
  json.dump(data, open('grid.json','w'))


