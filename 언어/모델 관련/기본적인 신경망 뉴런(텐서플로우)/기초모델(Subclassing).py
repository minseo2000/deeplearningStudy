import tensorflow as tf

class MyModel(tf.keras.Model):

    def __init__(self, hidden_dimension, hidden_dimension2, output_dimension):
        super(MyModel, self).__init__(name='My Model')
        self.hidden_dimension = hidden_dimension
        self.hidden_dimension2 = hidden_dimension2
        self.output_dimension = output_dimension

    def call(self, inputs):
        x = self.hidden_dimension(inputs)
        x = self.hidden_dimension2(x)

        return self.output_dimension(x)