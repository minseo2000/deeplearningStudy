import tensorflow as tf
from tensorflow.keras.utils import plot_model

(train_image, train_label), (test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()


print(train_image[:1])
print(train_label[:1])


train_image = train_image / 255.0
test_image = test_image / 255.0

print(train_image[:1])
print(train_label[:1])


model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape = (28, 28)),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(
    optimizer='adam',
    loss = 'sparse_categorical_crossentropy',
    metrics=['accuracy']
)

plot_model(model, to_file='./image.png')
