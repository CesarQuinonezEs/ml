from knn import KNN
import numpy as np
import matplotlib.pyplot as plt
from openFile import openAllFiles as op
from sklearn import datasets
from sklearn.model_selection import train_test_split
from matplotlib.colors import ListedColormap
cmap = ListedColormap(['#FF0000','#00FF00','#0000FF'])
X1 = op('colon-clear')
X2 = op('dyed-lifted-polyps')
X3 = op('stool-plenty')
y = [0,1,2]
iris = datasets.load_iris()
X, y = iris.data, iris.target
print(iris.target)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)


clf = KNN(k=5)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

acc = np.sum(predictions == y_test) / len(y_test)
print(acc)


