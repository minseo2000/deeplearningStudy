# Deep Learning Study files

# Working Contents
| To Do                                                                 | Date       | Hour |
|-----------------------------------------------------------------------|------------|------|
| mnist datasets by Sequential model                                    | 2023.10.10 | 2H   |
| mnist datasets by CNN model<br/>horse and person datasets by CNN model | 2023.10.17 | 2H   |
| 1. Image Generator<br/>2. 전이학습<br/>3. 드롭아웃 규제                         | 2023.10.17 | 1H   |
| tensorflow datasets<br/>tensorflow addons<br/>ETL Process             | 2023.10.18 | 1H   |


# 목차
1. Model Training Tips
2. Loss function and optimizer Tip
3. Datasets tips (tensorflow_datasets, tensorflow_addons)
4. ETL process

## basic_codes
1. fashion mnist classification files (early stopped, dense model)
2. fashion mnist classification file based cnn model


## Model Training Tips

| Category | Tips                                          | 효과      |
|----------|-----------------------------------------------|---------|
| CNN      | 1. Using ImageGenerator Class for Overfitting | 과대적합 방지 |
| CNN      | 2. Dropout Regulation                         | 과대적합 방지 |
| CNN      | 1. Using ImageGenerator Class for Overfitting |         |
| CNN      | 1. Using ImageGenerator Class for Overfitting |         |
| CNN      | 1. Using ImageGenerator Class for Overfitting |         |
| CNN      | 1. Using ImageGenerator Class for Overfitting |         |
| CNN      | 1. Using ImageGenerator Class for Overfitting |         |
| CNN      | 1. Using ImageGenerator Class for Overfitting |         |


## loss function and optimizer Tips

| 문제    | 손실함수                              | 출력층 뉴런 개수(활성화 함수)         |
|-------|-----------------------------------|---------------------------|
| 이진 분류 | 'binary_crossentopy'              | 뉴런 1개(소프트맥스 함수, 시그모이드 함수) |
| 다중 분류 | 'categorical_crossentropy'        | 뉴런 n개(소프트맥스 함수)           |
| 다중 분류 | 'sparse_categorical_crossentropy' | 뉴런 n개(소프트맥스 함수)           |

## Datasets Tips

- https://oreil.ly/zL7zq : 텐서플로 데이터 세트 사용 가능 목록<br>
사용을 위해서 아래 패키지 설치 할 것
```commandline
pip install tensorflow-datasets
```
- Using Example 1 (mnist_dataset)
```commandline
import tensorflow as tf
import tensorflow_datasets as tfds

# 텐서 데이터 세트에서 데이터를 불러오는 방법
(training_images, training_labes), (test_images, test_labels) = \ 
   tfds.as_numpy(tfds.load('fashion_mnist', split=['train', 'test'], batch_size=-1, as_supervised=True))


# 데이터 출력
for item in mnist_train.take(1):
    print(item['image'])
    print(item['label'])
# 상세 정보 출력
print(info)
```
- Using Example 2 (horses or humans datasets) and confirm dataset's version
```commandline
import tensorflow_datasets as tfds

data = tfds.load('horses_or_humans:3.0.0', split='train', as_supervised=True)
train_batches = data.shuffle(100).batch(10)
```

- 텐서플로우 애드온 사용 (이미지 증식 관련 함수 모음)
```commandline
pip install tensorflow-addons
```
- Example Codes
```commandline
import tensorflow_addons as tfa
data = tfds.load('horses_or_humans', split='train', as_supervised=True)

# 맵핑 함수 정의하기
def augmentimages(image, label):
    image = tf.cast(image, tf.float32)
    image = (image/255)
    image = tf.image.random_flip_left_right(image)
    image = tfa.image.rotate(image, 40, interpolation='NEAREST')
    return image, label

train = data.map(augmentimages)

train_batches = train.shuffle(100).batch(10)
```
- 데이터 슬라이싱 (아래와 같이 슬라이싱 가능)
```commandline
data = tfds.load('cats_vs_dogs', split='train', as_supervised=True)

data = tfds.load('cats_vs_dogs', split='train[:10000]', as_supervised=True)

data = tfds.load('cats_vs_dogs', split='train[:20%]', as_supervised=True)

data = tfds.load('cats_vs_dogs', split='train[-1000:]+train[:1000]', as_supervised=True)

# count items
train_length = [i for i, _ in enumerate(data)][-1] + 1
print(train_length)
```

# ETL Process (데이터 추출, 변환, 로드)
- 아래와 같이 구조 설계 시, 데이터나 모델 구조에 덜 민감하도록 데이터 파이프 라인을 만들 수 있다.
- example codes
```commandline
# 데이터 추출
data = tfds.load('horses_or_humans', split='train', as_supervised=True)
val_data = tfds.load('horses_or_humans', split='test', as_supervised=True)

# 데이터 변환
def augmentimages(image, label):
    image = tf.cast(image, tf.float32)
    image = (image/255)
    image = tf.image.random_flip_left_right(image)
    image = tfa.image.rotate(image, 40, interpolation='NEAREST')
    return image, label

# 데이터 로드
train = data.map(augmentimages)
train_batches = train.shuffle(100).batch(32)
validation_batches = val_data.batch(32)

```
