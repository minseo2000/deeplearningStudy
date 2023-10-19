# RNN과 RNN을 이용한 LSTM + 양방향 LSTM (여전히 단어 분류 문제?) -> 빈정거림


## WORD
| 이름         | 설명 |
|------------|----|
| RNN        |    |
| LSTM       ||
| 양방향 LSTM   ||
| Cell State ||

## RNN으로 텍스트 분류기 제작
```commandline
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(embedding_dim)),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

adam = tf.keras.optimizers.Adam(learning_rate=0.00001, beta_1=0.9, beta_2=0.999, amsgrad=False)



model.compile(
    loss = 'binary_crossentropy',
    optimizer=adam,
    metrics=['accuracy']
)

history = model.fit(training_padded, training_labels, epochs=30, validation_data=(testing_padded, testing_labels))
```