import tensorflow as tf
from tensorflow.keras.utils import plot_model

(train_image, train_label), (test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()


train_image = train_image / 255.0
test_image = test_image / 255.0

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

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('accuracy') > 0.95):
            print("\n 정확도 95%에 도달하여 훈련을 멈춥니다!")
            self.model.stop_training = True

callbacks = myCallback()

model.fit(
    train_image,
    train_label,
    epochs = 50,
    callbacks= [callbacks]
)

