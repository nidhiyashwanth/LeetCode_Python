class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D matrix with dimensions n x m to store the number of unique paths for each cell
        dp_matrix = [[1 for col in range(m)] for row in range(n)]
        
        # Iterate through each cell in the matrix starting from row 1 and column 1
        for row in range(1, n):
            for col in range(1, m):
                # Calculate the number of unique paths for the current cell by summing the number of paths from the left cell and the number of paths from the top cell
                dp_matrix[row][col] = dp_matrix[row][col - 1] + dp_matrix[row - 1][col]
        
        # Return the number of unique paths for the last cell in the matrix
        return dp_matrix[-1][-1]
