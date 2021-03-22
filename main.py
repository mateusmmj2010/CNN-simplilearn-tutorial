# This is a sample Convolution Neural Network.
import tensorflow
import matplotlib.pypolt as plt

from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense


# import datasets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# reshape datasets
x_train = x_train.reshape(60000,28,28,1)
x_test = x_test(10000,28,28,1)

# convert vector integer to binary vector
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# building CNN
model = Sequential()

# add first layer
model.add(Conv2D(64, kernel_size = 3, activation = 'relu', input_shape = (28,28,1)))
model.add(Conv2D(32, kernel_size = 3, activation = 'relu'))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

# compile CNN
model.compile(optmizer='adam', loss='category_crossentropy', metrics=['accuracy'])

# training model
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=3)

# use model to make predictions - first 10
model.predict(x_test[:10])