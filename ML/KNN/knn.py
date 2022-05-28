from sklearn.neighbors import KNeighborsClassifier
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

print("[INFO] informacje o macierzy i pamięci: {:.1f}MB"
      .format(data.nbytes / (64 *64.0)))

le=LabelEncoder()
labels = le.fit_transform(labels)

(trainX, testX, trainY, testY)=train_test_split(data,labels,
                                                test_size=.25, random_state=42)
print("[INFO] ewaluacja klasyfikatora k-NN... ")
model=KNeighborsClassifier(n_neighbors=args["neighbors"],
                           n_jobs=args["jobs"])

model.fit(trainX,trainY)
print(classification_report(testY,model.predict(testX),target_names=le.classes_))


