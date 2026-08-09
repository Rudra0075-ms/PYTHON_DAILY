import numpy as np
data = np.array([1, 2, 3, 4, 5])

mean = np.mean(data)
std_dev = np.std(data)

normalized_data = (data - mean) / std_dev
print("Normalized data:", normalized_data)

