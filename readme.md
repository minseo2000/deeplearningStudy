# Deep Learning Study files

# Working Contents
| To Do                                                                                                                                                        | Date       | Hour | REPO LINK                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|------|---------------------------------------------------------------------------|
| mnist datasets by Sequential model                                                                                                                           | 2023.10.10 | 2H   | https://github.com/minseo2000/deeplearningStudy/tree/master/basic_codes   |
| mnist datasets by CNN model<br/>horse and person datasets by CNN model                                                                                       | 2023.10.17 | 2H   | https://github.com/minseo2000/deeplearningStudy/tree/master/cnn_filter_codes |
| 1. Image Generator<br/>2. 전이학습<br/>3. 드롭아웃 규제                                                                                                                | 2023.10.17 | 1H   |                                                                           |
| tensorflow datasets<br/>tensorflow addons<br/>ETL Process                                                                                                    | 2023.10.18 | 1H   |                                                                           |
| Word Embedding ( NLP )                                                                                                                                       | 2023.10.19 | 1H   | https://github.com/minseo2000/deeplearningStudy/tree/master/embedding_codes |
| 1. Learning rate<br/>2. vocab_size<br/>3. Embedding Dimenssion<br/>4. Model Structure<br/>5. Dropout<br/> 6. Regulation<br/>7. Tensorflow Embedding Projector | 2023.10.20 | 1H   |                                                                           |
| RNN, LSTM, Bidirectional-LSTM                                                                                                                                | 2023.10.20 | 1H   |                                                                           |
| 문자기반, 단어기반 생성 모델 by LSTM                                                                                                                                     | 2023.10.20 | 1H   |                                                                           |


# DEEP LEARNING WORDS
| Name    | Description    |
|---------|----------------|
| Auto ML | 하이퍼파라미터 자동 학습? |



# 목차
1. Model Training Tips
2. Loss function and optimizer Tip
3. Datasets tips (tensorflow_datasets, tensorflow_addons)
4. ETL process
5. NLP Words
6. CSV FILE LOADER
7. Graph_codes
8. Embedding 시각화 codes

## basic_codes
1. fashion mnist classification files (early stopped, dense model)
2. fashion mnist classification file based cnn model


## Model Training Tips

| Category  | Tips                                          | 효과      | Image | 주의사항                    |
|-----------|-----------------------------------------------|---------|-------|-------------------------|
| CNN       | 1. Using ImageGenerator Class for Overfitting | 과대적합 방지 |       |                         |
| CNN       | 2. Dropout Regulation                         | 과대적합 방지 |       | 뉴런의 개수가 적다면 좋은 방법은 아니다.<br/> |
| Embedding | 3. Optimizer's Learning Rate                  | 과대적합 방지 |       |                         |
| Embedding | 4. 어휘사전을 구성할 때 특정단어가 많이 발생하는 어휘사전을 사용한다면?     | 과대적합 방지 |       |                         |
| Embedding | 5. 어휘사전의 4제곱근을 한 수를 차원의 수로 사용하라!              | 과대적합 방지 |       |                         |
| CNN       | 1. Using ImageGenerator Class for Overfitting |         |       |                         |
| CNN       | 1. Using ImageGenerator Class for Overfitting |         |       |                         |
| CNN       | 1. Using ImageGenerator Class for Overfitting |         |       |                         |



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

# NLP Words

| word                     | 설명                                       |
|--------------------------|------------------------------------------|
| 토큰                       | {'is' : 1, 'day' : 2}                    |
| 시퀀스                      | [[3,1,4,5,2]]                            |
| OOV(out of vocabulary)토큰 | 없는 데이터를 표현하는 토큰                          |
| 프리패딩                     | 짧은 문장을 긴 문장의 길이에 맞추기 위해 시작 부분을 0으로 채우는 것 |

# CSV FILE LOADER



# Graph_codes
```commandline
# graph codes
import matplotlib.pyplot as plt

def show_graph(history):
    # 그래프 출력 
    # 훈련 과정 기록 가져오기
    train_loss = history.history['loss']
    val_loss = history.history['val_loss']
    train_acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    # 그래프 출력
    epochs = range(1, len(train_loss) + 1)

    # 손실 그래프
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(epochs, train_loss, 'b', label='Training Loss')
    plt.plot(epochs, val_loss, 'r', label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    # 정확도 그래프
    plt.subplot(1, 2, 2)
    plt.plot(epochs, train_acc, 'b', label='Training Accuracy')
    plt.plot(epochs, val_acc, 'r', label='Validation Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.show()
```

# Embedding 시각화 codes
```commandline
import io

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

e = model.layers[0]
weights = e.get_weights()[0]
print(weights.shape)
out_v = io.open('vecs.tsv', 'w', encoding='utf-8')
out_m = io.open('meta.tsv', 'w', encoding='utf-8')

for word_num in range(1, vocab_size):
    word = reverse_word_index[word_num]
    embeddings = weights[word_num]
    out_m.write(word+'\n')
    out_v.write('\t'.join([str(x) for x in embeddings])+'\n')

out_v.close()
out_m.close()
```