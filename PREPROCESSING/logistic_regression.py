from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.model_selection import train_test_split
import numpy as np

# seed for reproducing same results
seed = 9
np.random.seed(seed)

# load pima indians dataset
dataset = np.loadtxt('autoencoded_input_1519054286.414525.csv', delimiter=',')

# split into input and output variables
X = dataset[:,0:4]
Y = dataset[:,4]

# split the data into training (67%) and testing (33%)
(X_train, X_test, Y_train, Y_test) = train_test_split(X, Y, test_size=0.33, random_state=seed)

# create the model
model = Sequential()
model.add(Dense(4, input_dim=4, init='uniform', activation='sigmoid'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

# compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the model
model.fit(X_train, Y_train, validation_data=(X_test, Y_test), nb_epoch=100, batch_size=1000)

# evaluate the model
scores = model.evaluate(X_test, Y_test)
print ("Accuracy: %.2f%%" %(scores[1]*100))


