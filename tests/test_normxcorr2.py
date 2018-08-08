import unittest

from scipy.io import loadmat
import numpy as np

from pymlfunc import normxcorr2
from pymlfunc import tictoc


class Test(unittest.TestCase):
    def _testxcorr2(self, template, image, result):
        with tictoc('Template size = {}, image size = {}'.format(template.shape, image.shape)):
            result_ = normxcorr2(template, image)

        self.assertTrue(np.allclose(result_, result))

    def testxcorr2_small(self):
        saved = loadmat('tests/normxcorr2.mat')
        a1 = saved['a1'].astype(np.float)
        c1 = saved['c1'].astype(np.float)
        template1 = saved['template1'].astype(np.float)

        self._testxcorr2(template1, a1, c1)

    def testxcorr2_big(self):
        saved = loadmat('tests/normxcorr2.mat')
        a2 = saved['a2'].astype(np.float)
        c2 = saved['c2'].astype(np.float)
        template2 = saved['template2'].astype(np.float)

        self._testxcorr2(template2, a2, c2)
