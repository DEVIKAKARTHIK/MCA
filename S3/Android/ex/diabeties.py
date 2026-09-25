#write a python program to predict diabetes using knn classification
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, r2_score


diabetes = load_diabetes()

print(diabetes.data.shape)
print(diabetes.feature_names)

X = diabetes.data
y = diabetes.target 

# print("data at 0",diabetes.data[0])

classifier = neighbors.KNeighborsRegressor(n_neighbors=5)

X_train,X_test  ,y_train  , y_test = train_test_split(X,y,test_size=0.3)

classifier.fit(X_train,y_train)

predition = classifier.predict(X_test)

# predition = classifier.predict([[1,3,4,5,6,7,8,9,10,11]])

print(predition)

# print(diabetes.target_names[predition])
# print("accuracy =", accuracy_score(y_test, predition) *(100))
print("Mean Squared Error:", mean_squared_error(y_test, predition))
print("R2 Score:", r2_score(y_test, predition))

