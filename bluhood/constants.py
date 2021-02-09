import numpy as np


B = 7
M = 71

ORDS = np.concatenate((
    np.array([1008]),
    np.array(range(32, 127)),
    np.array(range(7, 11))
))

KEYORDS = np.concatenate((ORDS[1:6], ORDS[17:60], ORDS[66:92]))
