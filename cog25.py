def all_paths(rows, cols):

    result = []

    def backtrack(row, col, path):

        # Reached bottom-right
        if row == rows - 1 and col == cols - 1:
            result.append(path)
            return

        # Move Right
        if col + 1 < cols:
            backtrack(row, col + 1, path + "R")

        # Move Down
        if row + 1 < rows:
            backtrack(row + 1, col, path + "D")

    backtrack(0, 0, "")

    return result


print(all_paths(2, 2))