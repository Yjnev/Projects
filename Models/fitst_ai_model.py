import tensorflow as tf
import numpy as np

X = np.array([1, 2, 3, 4], dtype=float)  # Input
Y = np.array([2, 4, 6, 8], dtype=float)  # Y = 2X

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1]) 
])

model.compile(optimizer='sgd', loss='mean_squared_error')

print("Training the model...")
model.fit(X, Y, epochs=500, verbose=0)  

print("Testing the model...")
result = model.predict(np.array([10.0])) 
print(f"The model predicts: {result[0][0]}")
