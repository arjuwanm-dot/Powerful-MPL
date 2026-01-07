import time
import os
import platform
import numpy as np
import matplotlib.pyplot as plt
import tracemalloc

# ----------------------------
# Reproducibility
# ----------------------------
np.random.seed(1)

# ----------------------------
# Start runtime & memory tracking
# ----------------------------
start_time = time.time()
tracemalloc.start()

# ----------------------------
# Load and preprocess image
# ----------------------------
image_path = "images/GFM1.jpg"
X_img = plt.imread(image_path)
X = np.array(X_img)

# Normalize and reshape
X = X.reshape(-1, 1) / 255.0
Y = np.array([[1]])

n_x = X.shape[0]
n_h = 5
n_y = 1

# ----------------------------
# Model initialization
# ----------------------------
def initialize_parameters(n_x, n_h, n_y):
    np.random.seed(1)
    return {
        "W1": np.random.randn(n_h, n_x) * 0.01,
        "b1": np.zeros((n_h, 1)),
        "W2": np.random.randn(n_y, n_h) * 0.01,
        "b2": np.zeros((n_y, 1)),
    }

def sigmoid(Z):
    return 1 / (1 + np.exp(-Z))

def relu(Z):
    return np.maximum(0, Z)

def forward(X, params):
    Z1 = params["W1"].dot(X) + params["b1"]
    A1 = relu(Z1)
    Z2 = params["W2"].dot(A1) + params["b2"]
    A2 = sigmoid(Z2)
    return A2

# ----------------------------
# Run forward pass
# ----------------------------
parameters = initialize_parameters(n_x, n_h, n_y)
output = forward(X, parameters)

# ----------------------------
# Stop memory & runtime tracking
# ----------------------------
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

end_time = time.time()

# ----------------------------
# System & resource reporting
# ----------------------------
print("===== Experiment Information =====")
print(f"OS: {platform.system()} {platform.release()}")
print(f"CPU cores: {os.cpu_count()}")
print(f"Random seed: 1")
print(f"Input dimension: {n_x}")
print(f"Peak Python memory usage: {peak / 1024**2:.2f} MB")
print(f"Total runtime: {(end_time - start_time):.2f} seconds")
print("==================================")
