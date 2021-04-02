import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

df = pd.read_csv("prime_Data.csv")

X = df.iloc[:, 1:].values  # bağımsız değişkenler
Y = df.iloc[:, 0]. values  # bağımlı değişkenler

X_egitim, X_test, Y_egitim, Y_test = train_test_split(
    X, Y, test_size=0.25, random_state=0)

sc = StandardScaler()
X_egitim = sc.fit_transform(X_egitim)
X_test = sc.fit_transform(X_test)


def RandomForest(X_egitim, Y_egitim):

    forest = RandomForestClassifier(
        n_estimators=10, criterion="entropy", random_state=0)
    forest.fit(X_egitim, Y_egitim)

    print("[0]Random Forest Classifier Training Accuracy:",
          forest.score(X_egitim, Y_egitim))

    return forest


model = RandomForest(X_egitim, Y_egitim)
cm = confusion_matrix(Y_test, model.predict(X_test))

TP = cm[1][1]
TN = cm[0][0]
FN = cm[1][0]
FP = cm[0][1]

print(cm)
print("Testing Accuracy = ", (TP + TN) / (TP + TN + FN + FP))

pred = model.predict(X_test)
print(pred)
print(Y_test)
