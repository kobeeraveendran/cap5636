import tensorflow as tf
from tensorflow.keras.layers import Flatten, Dense, Dropout, Softmax

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.Sequential([
    Flatten(input_shape = (28, 28)), 
    Dense(128, activation = 'relu'), 
    Dropout(0.2), 
    Dense(10), 
    Softmax()
])

untrained_predictions = model(x_train[:1]).numpy()

print("Predictions:\n", untrained_predictions)

pred_probs = tf.nn.softmax(untrained_predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True)
print("Untrained loss: ", loss_fn(y_train[:1], untrained_predictions).numpy())

model.compile(optimizer = 'adam', loss = loss_fn, metrics = ['accuracy'])

model.fit(x_train, y_train, epochs = 5)

model.evaluate(x_test, y_test, verbose = 2)