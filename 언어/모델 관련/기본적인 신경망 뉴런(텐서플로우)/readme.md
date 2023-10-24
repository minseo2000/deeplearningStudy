# 기본적인 신경망 층(텐서플로우)

| 이름        | 코드                        |
|-----------|---------------------------|
| Dense     | tf.keras.layers.Dense     |
| Dropout   | tf.keras.layers.Dropout   |
| Conv1D    | tf.keras.layers.Conv1D    |
| MaxPool1D | tf.keras.layers.MaxPool1D |

# 기본적인 모델 코드

| 이름                         | 코드                      | 문제점                                                                                           |
|----------------------------|-------------------------|-----------------------------------------------------------------------------------------------|
| Sequential                 | tf.keras.Sequential()   | 1. 다중 입력값 모델 사용x<br/>2. 다중 출력값 모델 사용x<br/>3. 공유 층을 활용하는 모델 사용x<br/>4. 데이터 흐름이 순차적이지 않은 모델 사용x |
| Functional API             | 기초모델(Functional API) 참고 |                                                                                               |
| Custom Layer               | 기초모델 (Custom Layer) 참고  | 신경망을 하나의 레이어로 묶어서 새로운 레이어로 만들고 싶다면 사용자 정의 층으로 만들자!                                            |
| Subclassing (Custom Model) | 기초모델(Subclassing) 참고    | 가장 자유도가 높은 모델 구현 방법이다!                                                                        |