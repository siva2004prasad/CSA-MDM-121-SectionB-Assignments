import numpy as np
import matplotlib.pyplot as plt

# Population: dice rolls
population = np.random.randint(1, 7, 10000)

sample_means = []
for _ in range(2000):
    sample = np.random.choice(population, size=50, replace=True)
    sample_means.append(np.mean(sample))

plt.hist(sample_means, bins=30, color='skyblue', edgecolor='black')
plt.title("Central Limit Theorem Demonstration")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()
