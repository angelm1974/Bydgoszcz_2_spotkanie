from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
from keras.models import Sequential
from keras.optimizers import sgd_experimental
from keras.layers import Dense
from keras.datasets import cifar10
import matplotlib.pyplot as plt
import argparse
import numpy as np

ap=argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
                help="sciezka do wystawienia wykresu")

args=vars(ap.parse_args())

print("[INFO] ładowanie biblioteki Cifar-10...")
((trainX,trainY),(testX,testY))=cifar10.load_data()
trainX =trainX.astype("float")/255.0
trainY =trainY.astype("float")/255.0

trainX=trainX.reshape((trainX.shape[0],3072))
testX=testX.reshape((testX.shape[0],3072))

lb=LabelBinarizer()
trainY=lb.fit_transform(trainY)
testY=lb.transform(testY)

etykiety =['samolot','samochod','ptak','kot','jelen','pies',
           'zaba','kon','owca','ciezarowka']

model=Sequential()
model.add(Dense(1024,input_shape=(3072,),activation="relu"))
model.add(Dense(512,activation="relu"))
model.add(Dense(10,activation="softmax"))

print("[INFO] trenowanie sieci...")
sgd=sgd_experimental(0.01)
model.compile(loss="categorical_crossentropy",optimizer=sgd,
              metrics=['accuracy'])
H = model.fit(trainX, trainY,validation_data=(testX,testY),
              epochs=100, batch_size=32)

print("[INFO] ewaluacja...")
predictions =model.predict(testX, batch_size=32)
print(classification_report(testY.argmax(axis=1),
                            predictions.argmax(axis=1),
                            target_names=etykiety))

plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0,100),H.history["loss"], label="strata przy trenowaniu")
plt.plot(np.arange(0,100),H.history["val_loss"], label="wartość straty")
plt.plot(np.arange(0,100),H.history["accuracy"], label="dopasowanie")
plt.plot(np.arange(0,100),H.history["val_accuracy"], label="wartość dopasowania")
plt.title("Trenowanie modelu i straty")
plt.xlabel("Epoka #")
plt.ylabel("strata/dokładność")
plt.legend()
plt.savefig(args["output"])

