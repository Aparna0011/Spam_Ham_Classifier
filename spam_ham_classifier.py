# -*- coding: utf-8 -*-
"""Spam_Ham_Classifier

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O47cwV4fsftBmPPMDI6wqGlrp7QHMCJh
"""

import pandas as pd

df=pd.read_csv("https://raw.githubusercontent.com/diazonic/Machine-Learning-using-sklearn/master/Datasets/spam.tsv",sep="\t")
df

df.head()

df[100:105]

df["label"].value_counts()

import matplotlib.pyplot as plt
df["label"].value_counts().plot(kind="bar")

plt.show()

df["label"].value_counts().plot(kind="bar",color="c")
a=df["label"].value_counts()
plt.text(0,a[0],a[0])
plt.text(1,a[1],a[1])
plt.show()

df.shape

df["message"][5568]

df["message"][5567]

x=df["message"].values
y=df["label"].values

x

y

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)

print(x_train.shape)
print(x_test.shape)

from sklearn.feature_extraction.text import CountVectorizer
vect=CountVectorizer(stop_words="english")

x_train_vect=vect.fit_transform(x_train)
x_test_vect=vect.transform(x_test)

from sklearn.svm import SVC
model=SVC()
model.fit(x_train_vect,y_train)

y_pred=model.predict(x_test_vect)

y_pred

from sklearn.metrics import accuracy_score

accuracy_score(y_test,y_pred)

from sklearn.metrics import classification_report
print(classification_report(y_pred,y_test))

test=df["message"][3000]
test

df["label"][3000]

test=vect.transform([df["message"][3000]])
model.predict(test)

test=df["message"][2003]
test

df["label"][2003]

test=vect.transform([df["message"][2003]])
model.predict(test)

from sklearn.pipeline import make_pipeline
text_model=make_pipeline(CountVectorizer(),SVC())
text_model.fit(x_train,y_train)
y_pred=text_model.predict(x_test)
y_pred

text_model.predict([df["message"][0]])

import joblib

joblib.dump(text_model,"spam-ham")

