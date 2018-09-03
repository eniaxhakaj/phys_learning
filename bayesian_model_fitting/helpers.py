import numpy as np

def add_bias_col(x):
    return np.vstack((x, np.ones(len(x)))).T
