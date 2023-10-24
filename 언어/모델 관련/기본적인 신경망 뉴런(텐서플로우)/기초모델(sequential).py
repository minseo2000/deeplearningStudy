import tensorflow as tf


model = tf.keras.Sequential()
# 요런 식으로 사이에 층 끼워넣기
model.add(tf.keras.layers.Dense(64, actication='relu'))

