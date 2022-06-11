from keras.applications.resnet import ResNet50
from keras.applications.inception_v3 import InceptionV3
from keras.applications.xception import Xception
from keras.applications.vgg16 import VGG16
from keras.applications.vgg19 import VGG19
from keras.applications import imagenet_utils
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from keras.applications.inception_v3 import preprocess_input

import numpy as np
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",required=True, 
                help="scieżka do obrazka z obiektem")
ap.add_argument("-model","--model",type=str, default="inception", 
                help="nazwa pretrenowanego modelu")

args=vars(ap.parse_args())


MODELS ={
    "vgg16": VGG16,
    "vgg19": VGG19,
    "inception": InceptionV3,
    "xception": Xception,
    "resnet": ResNet50
}

if args["model"] not in MODELS.keys():
    raise AssertionError(" Podanego ciągu znaków nie ma w słowniku modeli!!!")

inputShape =(224,224)

if args["model"] in("inception", "xception"):
    inputShape =(299,299)
preprocess=preprocess_input

print("[INFO] ładowanie {}...".format(args["model"]))
Network = MODELS[args["model"]]
model = Network(weights="imagenet")

print("[INFO] ładowanie i pre-processing naszego obrazu...")
image = load_img(args["image"],target_size=inputShape)
image = img_to_array(image)

image = np.expand_dims(image,axis=0)
image=preprocess(image)

#klasyfikacja
print("[INFO] klasyfikacja obrazu za pomocą {}...".format(args["model"]))
preds = model.predict(image)
P = imagenet_utils.decode_predictions(preds)

for (i, (imagenetID, label, prob)) in enumerate(P[0]):
    print("{}. {}: {:.2f}%".format(i+1,label,prob*100))

orig =cv2.imread(args["image"])
(imagenetID, label, prob)=P[0][0]
cv2.putText(orig, "Etykieta: {}".format(label),(10,30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0,255,0),2)
cv2.imshow("Klasyfikacja",orig)
cv2.waitKey(0)
    