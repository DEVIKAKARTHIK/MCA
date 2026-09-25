from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

iris = datasets.load_iris()

X, y = iris.data, iris.target

classifier = tree.DecisionTreeClassifier()

x_train, x_test, y_train, y_test = train_test_split(
    X, y, train_size=0.7, random_state=42
)

classifier.fit(x_train, y_train)

# Display decision tree
tree.plot_tree(
    classifier,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True
)

plt.show()

# Test the model
result = classifier.predict(x_test)

accuracy = accuracy_score(y_test, result) * 100
print(f'Accuracy is {accuracy:.2f}%')

# Take input from user
features = [[float(i) for i in input(
    f'Enter {iris.feature_names}: '
).split()]]

# Predict
result = classifier.predict(features)

print("Predicted flower:", iris['target_names'][result[0]])
