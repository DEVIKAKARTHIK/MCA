from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import numpy as np

iris = load_iris()

X = iris.data
y = iris.target

#split iris dataset into trainig and testing data

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2)

model = GaussianNB()


model.fit(X_train,y_train)

#preditions = model.predict(X_test)
y_prediction = model.predict(X_test)
print(y_prediction)
print(y_test)
print("accuracy score :\n",accuracy_score(y_test,y_prediction))
print("confusion matrix :\n",confusion_matrix(y_test, y_prediction))
print("classification report :\n",classification_report(y_test, y_prediction))

#new data
sample = np.array([[5.1,3.5,1.4,0.2]])
prediction = model.predict(sample)
print("new data predicted:",prediction)

# new data

sample1 = np.array([[5,4,3,3],[1,1,1,1]])
prediction1 = model.predict(sample1)
print("new data predicted:",prediction1)

print(iris.target_names[prediction1])



