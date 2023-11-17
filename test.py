
import pytest
from sparse_recommender import SparseMatrix

# Test cases for each function
def test_set():
    matrix = SparseMatrix()
    matrix.set(1, 1, 5)
    assert matrix.get(1, 1) == 5

def test_get():
    matrix = SparseMatrix()
    matrix.set(1, 1, 5)
    assert matrix.get(1, 1) == 5

def test_recommend():
    matrix = SparseMatrix()
    matrix.set(1, 1, 5)
    user_vector = [0, 1]
    assert matrix.recommend(user_vector) == [0, 5]

def test_add_movie():
    matrix1 = SparseMatrix()
    matrix1.set(1, 1, 5)
    matrix2 = SparseMatrix()
    matrix2.set(1, 1, 5)
    result = matrix1.add_movie(matrix2)
    assert result.get(1, 1) == 10

def test_to_dense():
    matrix = SparseMatrix()
    matrix.set(1, 1, 5)
    assert matrix.to_dense() == [[0, 0], [0, 5]]

# Edge Test Cases for empty value and negative indices
def test_get_from_empty_matrix():
    matrix = SparseMatrix()
    assert matrix.get(1, 1) is None, "Getting from an empty matrix should return None"

def test_set_negative_indices():
    matrix = SparseMatrix()
    with pytest.raises(ValueError):
        matrix.set(-1, 1, 5)
    with pytest.raises(ValueError):
        matrix.set(1, -1, 5)