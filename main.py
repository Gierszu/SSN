# Plik do różnych testów ogólnolabowych

import numpy as np


def calculate_l2(weights: np.ndarray, inputs: np.ndarray):
    return np.sum(np.dot(weights, inputs)**2)
