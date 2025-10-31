import numpy as np
from scipy.stats import skew, kurtosis

arr = np.array([5, 7, 8, 5, 6, 9, 12, 15])

data_range = np.max(arr) - np.min(arr)
variance = np.var(arr, ddof=1)   # sample variance
skewness = skew(arr)
kurt = kurtosis(arr)

print("Range:", data_range)
print("Variance:", variance)
print("Skewness:", skewness)
print("Kurtosis:", kurt)
