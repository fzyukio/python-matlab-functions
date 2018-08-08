import unittest

import numpy as np
from pymlfunc import sub2ind, ind2sub


def one_randint(limit=10):
    return np.random.randint(limit, size=1)[0]


class Test(unittest.TestCase):
    def setUp(self):
        nrows = one_randint(100)
        ncols = one_randint(100)
        nselected = one_randint(nrows)

        self.rows = np.random.randint(nrows, size=nselected)
        self.cols = np.random.randint(ncols, size=nselected)
        self.inds = np.random.randint(ncols * nrows, size=one_randint(nrows * ncols))

        self.mat = np.random.rand(nrows, ncols)

    def test_sub2ind(self):
        ind = sub2ind(self.mat.shape, self.rows, self.cols)
        self.assertTrue(np.allclose(self.mat[self.rows, self.cols], self.mat.ravel()[ind]))

    def test_ind2sub(self):
        rows, cols = ind2sub(self.mat.shape, self.inds)
        self.assertTrue(np.allclose(self.mat[rows, cols], self.mat.ravel()[self.inds]))
