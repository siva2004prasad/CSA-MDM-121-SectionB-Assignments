import numpy as np
from scipy.stats import ttest_ind

# Two sample groups
groupA = np.array([85, 88, 90, 92, 87, 91])
groupB = np.array([80, 82, 78, 85, 79, 81])

t_stat, p_val = ttest_ind(groupA, groupB)

print("T-statistic:", t_stat)
print("P-value:", p_val)

if p_val < 0.05:
    print("Result: Significant difference between groups")
else:
    print("Result: No significant difference between groups")
