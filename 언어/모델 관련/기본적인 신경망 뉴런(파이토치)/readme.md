# 기본적인 신경망층 (파이토치)


- 신경망 층

| 이름       | 코드                        |
|----------|---------------------------|
|          | tf.keras.layers.Dense     |
| Dropout  | tf.keras.layers.Dropout   |
| Conv1D   | tf.keras.layers.Conv1D    |
| MaxPool1D | tf.keras.layers.MaxPool1D |

- 활성화 함수

| 이름                 | 코드                 |
|--------------------|--------------------|
| Sigmoid            | torch.sigmoid      |
| hyperbolic tangent | torch.tanh         |
| relu               | torch.nn.ReLU()    |
| Prelu              | torch.nn.PReLU()   |
| softmax            | torch.nn.Softmax() |

- 손실함수

| 이름           | 코드                          |
|--------------|-----------------------------|
| 평균 제곱 오차     | torch.nn.MSELoss()          |
| 범주형 크로스 엔트로피 | torch.nn.CrossEntropyLoss() |
| 이진 크로스 엔트로피  | torch.nn.BCELoss()          |

- 옵티마이저

| 이름   | 코드               |
|------|------------------|
| Adam | torch.optim.Adam |



