def search_for_a_sequence(grid, sequence):
    def search_for_a_sequence_helper(row, col, index):
        if index == p :
            return True
        if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] != sequence[index] :
            return False
        path.append((row, col))
        if (row, col, index) in previous_attempts :
            return False
        #search right
        if not (row, col+1, index+1) in previous_attempts and search_for_a_sequence_helper(row, col+1, index+1) :
            return True
        #search left
        if not (row, col-1, index+1) in previous_attempts and search_for_a_sequence_helper(row, col-1, index+1):
            return True
        #search up
        if not (row-1, col, index+1) in previous_attempts and search_for_a_sequence_helper(row-1, col, index+1):
            return True
        #search down
        if not (row+1, col, index+1) in previous_attempts and search_for_a_sequence_helper(row+1, col, index+1) :
            return True
        previous_attempts.add((row, col, index)) #didn't worked
        path.pop() #backtrack
        return False

    n, m = len(grid), len(grid[0])
    p = len(sequence)
    previous_attempts = set()
    path = []
    return any (search_for_a_sequence_helper(i, j, 0) for i in range(n) for j in range(m))

if __name__ == "__main__":
    grid = [[1,2,3],[3,4,5],[5,6,7]]
    sequence = [1,3,4,6]
    print search_for_a_sequence(grid, sequence)



