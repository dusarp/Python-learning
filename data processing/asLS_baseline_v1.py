import numpy as np
from scipy.sparse import spdiags
from scipy.sparse.linalg import spsolve

def asLS_baseline_v1(signal, smoothness_param=1e3, asym_param=1e-4):
    # Estimate baseline with asymmetric least squares
    MIN_DIFF = 1e-6
    MAX_ITER = 100
    ORDER = 2

    signal_length = len(signal)
    signal = signal.reshape(-1, 1)

    if np.isscalar(smoothness_param):
        smoothness_param = smoothness_param * np.ones(signal_length)
    else:
        pass

    penalty_vector = np.ones(signal_length)

    difference_matrix = np.diff(np.eye(signal_length), n=ORDER, axis=0)

    smoothness_matrix = np.multiply(smoothness_param.reshape(-1, 1), np.ones((1, difference_matrix.shape[0])))

    differ = np.zeros(MAX_ITER)

    for count in range(MAX_ITER):
        Weights = spdiags(penalty_vector, 0, signal_length, signal_length)

        C = np.linalg.cholesky(Weights + smoothness_matrix @ difference_matrix.T @ difference_matrix)

        if count > 0:
            baseline_last = baseline.copy()

        baseline = spsolve(C.T, spsolve(C, penalty_vector * signal)).ravel()

        # Test for convergence
        if count > 0:
            differ[count] = np.sum(np.abs(baseline_last - baseline))
            if differ[count] < MIN_DIFF:
                break  # Change is negligible

        penalty_vector = asym_param * (signal.ravel() > baseline) + (1 - asym_param) * (signal.ravel() < baseline)

    return baseline