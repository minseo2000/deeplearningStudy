# 패션 MNist 분류
<hr>

## mnist_fashion_calssification.py
- 위 코드에서는 텐서플로 내장 데이터 세트인 fashion_mnist를 다룬다.
- 순차적인 신경망을 만들 수 있다.
- 조기 종료 알고리즘을 직접 만들 수 있다.
- 데이터 스케일링에 대해 알 수 있다.

## 단순한 맵핑 구조의 딥러닝

<img width="663" alt="image" src="https://github.com/minseo2000/deeplearningStudy/assets/59526414/e8a0d153-f08b-4db9-a7da-b1765f225519">


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
|    <img width="882" alt="load_data_result" src="https://github.com/minseo2000/deeplearningStudy/assets/59526414/7a11f983-a23a-431f-85fb-7b84d1036a04">
          |
<hr>

- Data Scaling

```commandline
train_image = train_image / 255.0
test_image = test_image / 255.0
```

-> result

| Result Image |
|--------------|
|      <img width="882" alt="data_scaling_result" src="https://github.com/minseo2000/deeplearningStudy/assets/59526414/174009ca-5ba3-4d47-945a-2843b496b26e">
        |

<hr>

- early stopped algorithm codes <br>
클래스를 선언해서, on_epoch_end 함수를 정의해서 조기종료 함수를 만들어 줄 수 있다.
```commandline

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

```

-> result

| Result Image |
|--------------|
|    <img width="741" alt="early_stop" src="https://github.com/minseo2000/deeplearningStudy/assets/59526414/63916609-bbe7-40de-a4d3-ad5aa8c98720">|

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
|     <img width="522" alt="model_result" src="https://github.com/minseo2000/deeplearningStudy/assets/59526414/bac6763e-61b3-4d11-94b1-546925eec75c">|
|<img width="756" alt="train_result" src="https://github.com/minseo2000/deeplearningStudy/assets/59526414/ec958dcb-0c0b-428a-bb87-9af556469211">|


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
|     ![model_image](https://github.com/minseo2000/deeplearningStudy/assets/59526414/82684255-79b1-4e07-b624-55c7c2730a51)|



