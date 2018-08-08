from __future__ import print_function
import numpy as np
from scipy.signal import fftconvolve


def shift_data(arr):
    min_arr = np.min(arr)
    if min_arr < 0:
        arr -= min_arr
    return arr


def normxcorr2(template, image):
    """
    Computes the normalised cross-correlation of matrices template and image.
    The matrix image must be larger than the matrix template
    The resulting matrix contains correlation coefficients and its values may range from -1.0 to 1.0.

    :param template: the smaller matrix to be cross-correlated with the image.
    :param image: the bigger matrix
    :return: N-D matrix contains correlation coefficients and its values may range from -1.0 to 1.0.
    """
    if np.ndim(template) > np.ndim(image) or \
            len([i for i in range(np.ndim(template)) if template.shape[i] > image.shape[i]]) > 0:
        raise ValueError("Template larger than image. Arguments are swapped.")

    template = shift_data(template)
    image = shift_data(image)

    cross_corr = fftconvolve(np.rot90(template, 2), image)
    m, n = template.shape
    mn = m * n

    local_sum_A2 = local_sum(image ** 2, m, n)
    local_sum_A = local_sum(image, m, n)

    diff_local_sums = (local_sum_A2 - (local_sum_A ** 2) / mn)
    denom_A = np.sqrt(np.maximum(diff_local_sums, 0))

    denom_T = np.sqrt(mn - 1) * np.std(template, ddof=1)
    denom = denom_T * denom_A
    numerator = cross_corr - local_sum_A * template.sum() / mn

    out = np.zeros(numerator.shape)
    tol = np.sqrt(np.spacing(np.max(np.abs(denom))))
    i_nonzero = np.where(denom > tol)
    out[i_nonzero] = numerator[i_nonzero] / denom[i_nonzero]

    out[np.where((np.abs(out) - 1) > np.sqrt(np.spacing(1)))] = 0
    return out


def local_sum(A, m, n):
    B = np.pad(A, ((m, m), (n, n)), mode='constant', constant_values=0)
    s = np.cumsum(B, axis=0)
    c = s[m:-1, :] - s[:-m - 1, :]
    s = np.cumsum(c, axis=1)
    local_sum_A = s[:, n:-1] - s[:, :-n - 1]
    return local_sum_A
