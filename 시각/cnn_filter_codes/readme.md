# mnist fashion_data Classification

## codes

<hr>

- CNN Model Codes

```commandline
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax),
])

```
-> result

| Result Image |
|--------------|
|   |
<hr>

## Errors
<hr>

### 모델이 학습을 하지 못할 때

-> 다음 상황 일 때

1. 모델의 Output Layer, 활성화 함수를 확인해보자.