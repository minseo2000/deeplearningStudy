# 패션 MNist 분류
<hr>

## mnist_fashion_calssification.py
- 위 코드에서는 텐서플로 내장 데이터 세트인 fashion_mnist를 다룬다.
- 순차적인 신경망을 만들 수 있다.
- 조기 종료 알고리즘을 직접 만들 수 있다.
- 데이터 스케일링에 대해 알 수 있다.

## About Codes

- load fashion_mnist data

```commandline
import tensorflow as tf

(train_image, train_label), (test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()


print(train_image[:1])
print(train_label[:1])
```
-> result

| Result Image |
|--------------|
|              |
<hr>

- Data Scaling

```commandline
train_image = train_image / 255.0
test_image = test_image / 255.0
```

-> result

| Result Image |
|--------------|
|              |

<hr>

- early stopped algorithm codes
```commandline

```

-> result

| Result Image |
|--------------|
|              |

<hr>

- model codes
```commandline
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

model.summary()

model.fit(
    train_image,
    train_label,
    epochs=5
)

model.evaluate(
    test_image,
    test_label
)
```

-> result

| Result Image |
|--------------|
|              |

<hr>

- model Structure <br>

before use this you have to install "pydot" and "graphviz program"

```commandline
from tensorflow.keras.utils import plot_model
plot_model(model)
```

-> result

| Result Image |
|--------------|
|              |

