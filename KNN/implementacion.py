from knn import KNN
import numpy as np
#import matplotlib.pyplot as plt
from openFile import openAllFiles as op
from sklearn import datasets
from sklearn.model_selection import train_test_split
#from matplotlib.colors import ListedColormap
X1 = op('training/colon-clear')
#cmap = ListedColormap(['#FF0000','#00FF00','#0000FF'])
X2 = op('training/dyed-lifted-polyps')
X3 = op('training/stool-plenty')
Xaux = np.concatenate((X1,X2))
X_train = np.concatenate((Xaux,X3))

Y1 = np.full(30,0)
Y2 = np.full(30,1)
Y3 = np.full(30,2)
Yaux = np.concatenate((Y1,Y2))
y_train = np.concatenate((Yaux, Y3))


X1_test = op('test/colon-clear')
X2_test = op('test/dyed-lifted-polyps')
X3_test = op('test/stool-plenty')
Xaux = np.concatenate((X1_test,X2_test))
X_test = np.concatenate((Xaux,X3_test))

Y1 = np.full(len(X1_test),0)
Y2 = np.full(len(X2_test),1)
Y3 = np.full(len(X3_test),2)
Yaux = np.concatenate((Y1,Y2))
y_test = np.concatenate((Yaux, Y3))


clf = KNN(k=3)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
acc = np.sum(predictions == y_test) / len(y_test)
press = np.sum(predictions == y_test) /  (np.sum(predictions == y_test) + np.sum(predictions != y_test))
recall = np.sum(predictions == y_test) /  (np.sum(predictions == y_test) + np.sum(predictions != y_test))
score = (2*(recall*press))/(press+recall)
print("exactitud ",acc)
print("precisión ",press)
print("Recuerdo ",recall)


