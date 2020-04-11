import logging
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

logger = tf.get_logger()
logger.setLevel(logging.ERROR)

# input to the model - features
celsius_q = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
# labels - output
fahrenheit_a = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

for i, c in enumerate(celsius_q):
    print("{} degrees Celsius = {} degrees Fahrenheit".format(c, fahrenheit_a[i]))

# layers of the tf network
number_of_layers = 5
if number_of_layers > 1:
    l0 = tf.keras.layers.Dense(units=2, input_shape=[1])
    l1 = tf.keras.layers.Dense(units=4)
    l2 = tf.keras.layers.Dense(units=8)
    l3 = tf.keras.layers.Dense(units=4)
    l4 = tf.keras.layers.Dense(units=1)
    model = tf.keras.Sequential([l0, l1, l2, l3, l4])
else:
    l0 = tf.keras.layers.Dense(units=1, input_shape=[1])
    model = tf.keras.Sequential([l0])

model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
history = model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
print("Finished training the model")

plt.xlabel('Epoch Number')
plt.ylabel('Loss Magnitude')
plt.plot(history.history['loss'])
plt.show()

print(model.predict([100.0]))
print("These are the layer variables: {}".format(l0.get_weights()))
