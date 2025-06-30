#creat a simple sudoku game with a 9x9 grid
class Sudoku:
    def __init__(self, grid):
        self.grid = grid

    def is_valid(self, row, col, num):
        # Check if the number is not in the current row
        if num in self.grid[row]:
            return False
        
        # Check if the number is not in the current column
        for r in range(9):
            if self.grid[r][col] == num:
                return False
        
        # Check if the number is not in the current 3x3 subgrid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if self.grid[r][c] == num:
                    return False
        
        return True

    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:  # Find an empty cell
                    for num in range(1, 10):  # Try numbers from 1 to 9
                        if self.is_valid(row, col, num):
                            self.grid[row][col] = num  # Place the number
                            if self.solve():  # Recursively try to solve
                                return True
                            self.grid[row][col] = 0  # Reset on backtrack
                    return False  # No valid number found, backtrack
        return True  # Solved successfully

    def print_grid(self):
        for row in self.grid:
            print(" ".join(str(num) for num in row))
# Example usage
if __name__ == "__main__":
    sudoku_grid = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [8, 9, 1, 2, 3, 4, 5, 6, 0],
        [9, 1, 2, 3, 4, 5, 6, 7, 0]
    ]
    
    sudoku = Sudoku(sudoku_grid)
    if sudoku.solve():
        sudoku.print_grid()
    else:
        print("No solution exists.")  
  
