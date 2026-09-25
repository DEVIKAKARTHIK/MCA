from sklearn.datasets import load_iris
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np

iris = load_iris()

X = iris.data
y = iris.target

X_train , X_test , y_train ,y_test = train_test_split(X,y,test_size=0.3,random_state=43)

classifier = neighbors.KNeighborsClassifier(n_neighbors=3)


classifier.fit(X_train,y_train)

# prediction = classifier.predict(X_test)

# print("accuracy_score = ",accuracy_score(y_test,prediction))
# for pred in prediction:
#  print(iris.target_names[pred])

sample = np.array([[1,3,1,1]])
prediction = classifier.predict(sample)
print(iris.target_names[prediction])
# print("accuracy_score:",)

