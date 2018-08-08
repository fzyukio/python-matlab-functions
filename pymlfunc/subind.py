def sub2ind(array_shape, rows, cols):
    """
    Equivalent to the same-named function in Matlab (Except that Matlab is Fortran-styled indexing)
    Usage:
    In Matlab:
    A = reshape(1:30, 6, [])
    sub2ind(size(A), [2, 4], [1, 3])
    ans = 2    16

    Equivalently, in python:
    >>> mat = np.arange(1, 31).reshape((5, 6))
    >>> ind = sub2ind(mat.shape, np.array([0, 2]), np.array([1, 3]))
    >>> array([ 1, 15])

    Notice that the row and column arrays are swapped, and the indices are 1 less than that in Matlab,
    e.g. [1, 3] => [0, 2]

    :param array_shape:
    :param rows:
    :param cols:
    :return:
    """
    ind = rows * array_shape[1] + cols
    ind[ind < 0] = -1
    ind[ind >= array_shape[0] * array_shape[1]] = -1
    return ind


def ind2sub(array_shape, ind):
    """
    Equivalent to the same-named function in Matlab (Except that Matlab is Fortran-styled indexing)
    :param array_shape:
    :param rows:
    :param cols:
    :return:
    """
    ind[ind < 0] = -1
    ind[ind >= array_shape[0] * array_shape[1]] = -1
    rows = (ind.astype('int') // array_shape[1])
    cols = ind % array_shape[1]
    return rows, cols
