# -*- coding: utf-8 -*-
"""heart failure

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ITg3OaqQ_x7fbgnM7lGiL-o4zUfYtmlO
"""

import pandas as pd
import numpy as np
import matplotlib as plt

dataset=pd.read_csv("/content/heart_failure_clinical_records_dataset.csv")
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=1)

from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
x_train=ss.fit_transform(x_train)
x_test=ss.fit_transform(x_test)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1))

from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix
print(cm(y_test,y_pred))
accuracy_score(y_test,y_pred)