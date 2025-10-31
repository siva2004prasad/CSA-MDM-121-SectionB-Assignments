import numpy as np
from scipy import stats

# Example data: hours studied vs marks
hours = np.array([2, 3, 4, 5, 6, 7])
marks = np.array([50, 55, 60, 65, 70, 78])

# Correlation
corr = np.corrcoef(hours, marks)[0, 1]

# Regression
slope, intercept, r_val, p_val, std_err = stats.linregress(hours, marks)

print("Correlation Coefficient:", corr)
print("Regression Line: y =", slope, "* x +", intercept)
