class SparseMatrix:
    def __init__(self):
        self.data = {}

    def set(self, row, col, value):
        if not hasattr(self, 'data'):
            self.data = {}
        if row not in self.data:
            self.data[row] = {}
        self.data[row][col] = value

    def get(self, row, col):
        return self.data.get(row, {}).get(col, 0)

    # Method to recommend a movie based on a user vector.
    def recommend(self, vector):
        result = [0] * len(vector)
        for row, cols in self.data.items():
            for col, value in cols.items():
                result[row] += value * vector[col]
        return result

    # Method to add another sparse matrix.
    def add_movie(self, matrix):
        result = SparseMatrix()
        for row, cols in self.data.items():
            for col, value in cols.items():
                result.set(row, col, value + matrix.get(row, col))
        return result

    # Converting sparse matrix to a dense matrix.
    def to_dense(self):
        max_row = max(self.data.keys()) + 1
        max_col = max(max(cols.keys()) for cols in self.data.values()) + 1
        result = [[0] * max_col for _ in range(max_row)]
        for row, cols in self.data.items():
            for col, value in cols.items():
                result[row][col] = value
        return result
    
    # Additional Edge Cases
    def set(self, row, col, value):
        if row < 0 or col < 0:
            raise ValueError("Row and column indices must be non-negative")
        if row not in self.data:
            self.data[row] = {}
        self.data[row][col] = value

    def get(self, row, col):
        return self.data.get(row, {}).get(col, None)

