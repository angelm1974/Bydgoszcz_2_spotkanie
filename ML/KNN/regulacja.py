from random import random
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imagesearch.preprocessing import SimplePreprocessor
from imagesearch.datasets import SimpleDatasetLoader
from imutils import paths
import argparse

ap=argparse.ArgumentParser()

ap.add_argument("-d", "--dataset",
                required=True,help="ścieżka do naszych obrazków")

ap.add_argument("-k","--neighbors",type=int, 
                default=1, help="# ilość najbliższych sąsiadów używana  w klasyfikacji")

ap.add_argument("-j","--jobs",type=int, default=-1, help="# ilość wątków dla KNN")

args=vars(ap.parse_args())


print("[INFO] - ładowanie obrazów...")
imagePaths = list(paths.list_images(args["dataset"]))


sp =SimplePreprocessor(64, 64)
sdl = SimpleDatasetLoader(preprocessors=[sp])
(data, labels)= sdl.load(imagePaths,verbose=500)
data=data.reshape((data.shape[0],12288))

le=LabelEncoder()
labels = le.fit_transform(labels)

(trainX, testX, trainY, testY)=train_test_split(data,labels,
                                                test_size=.25, random_state=42)

for r in(None,"l1","l2"):
    print("[INFO] trenujemy model z progiem błędu `{}`".format(r))
    model=SGDClassifier(loss="log",penalty=r,max_iter=15,
                        learning_rate="optimal",tol=1e-4,eta0=0.01,random_state=12)
    
    model.fit(trainX,trainY)
    acc=model.score(testX,testY)
    print("[INFO] `{}` dokładność: {:.2f}%".format(r, acc*100))