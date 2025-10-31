import statistics as st

data = [12, 15, 20, 20, 18, 22, 25]

# Basic measures
mean_val = sum(data) / len(data)   # manual mean
median_val = st.median(data)       # library median
mode_val = st.multimode(data)      # multimode for multiple modes

# Weighted mean
weights = [1, 2, 1, 1, 2, 1, 2]
weighted_mean = sum(x*w for x, w in zip(data, weights)) / sum(weights)

print("Mean:", mean_val)
print("Median:", median_val)
print("Mode(s):", mode_val)
print("Weighted Mean:", weighted_mean)
