#implement guassian np using the public dataset load_breast_cancer 

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score

BCancer = load_breast_cancer()
# print(model.target_names)
# print(model.feature_names)

X = BCancer.data
y = BCancer.target

X_train , X_test , y_train, y_test = train_test_split(X,y,test_size=0.2)

model = GaussianNB()

model.fit(X_train,y_train)

predict = model.predict(X_test)

print(predict)
print("Accuracy : ",accuracy_score(y_test,predict))
print("confusion : ",confusion_matrix(y_test,predict))
print("classification_report:",classification_report(y_test,predict))


# print(model.)
# print(load_breast_cancer)

sample = X_test[0].reshape(1,-1)
print(sample)
prediction = model.predict(sample)
print(prediction)
print(BCancer.target_names[prediction])