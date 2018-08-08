from __future__ import print_function
from contextlib import contextmanager

import time


@contextmanager
def tictoc(function_name):
    start = time.time()
    yield
    end = time.time()
    print('{0:s}: finished in {1: 9.9f} seconds'.format(function_name, end - start))
