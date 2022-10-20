import numpy as np
#nila gayatri
#21091397066

inputs = [3.0, 4.0, 3.1, 2.3, 5.5, 6.3, 5.5, 9.5, 3.4, 5.5]
weights = [2.2, 1.2, 3.3, 1.6, 1.5, 6.2, 2.4, 9.2, 0.5, 3.4]
#neuron 1
bias = 3.5

outputs = np.dot(weights, inputs) + bias
print(outputs)
