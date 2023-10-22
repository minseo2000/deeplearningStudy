import tensorflow as tf

data_loader = tf.keras.datasets.fashion_mnist

(train_image, train_label), (test_image, test_label) = data_loader.load_data()

train_image = train_image.reshape(60000, 28, 28, 1)
test_image = test_image.reshape(10000, 28, 28, 1)

train_image = train_image / 255.0
test_image = test_image / 255.0


model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax),
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
              )

model.fit(
    train_image,
    train_label,
    epochs=50
)

model.evaluate(test_image, test_label)
