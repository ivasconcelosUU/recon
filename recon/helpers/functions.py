import numpy as np
import scipy.sparse.linalg

def is_numeric(obj):
    attrs = ['__add__', '__sub__', '__mul__', '__truediv__', '__pow__']
    return all(hasattr(obj, attr) for attr in attrs)

def is_vector(obj):
    if (len(obj.shape) == 1 or obj.shape[1] == 1):
        return True
    elif (len(obj.shape) == 2 and obj.shape[1] == 1):
        return True
    else:
        return False

def is_scalar(obj):
    if np.isscalar(obj):
        return True
    else:
        return False

def switch_arguments(arg1, arg2):
    return arg2, arg1

def normest(K):
    _, s, _ = scipy.sparse.linalg.svds(K, k=1)
    return s[0]