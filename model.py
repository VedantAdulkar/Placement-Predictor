from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle
import torch
import numpy as np
import sklearn

df = pd.read_csv('C:/Users/Vedant/Desktop/app/placedata.csv')

df['PlacementTraining'] = df['PlacementTraining'].apply(lambda x: 1 if x=='Yes' else 0)
df['ExtracurricularActivities'] = df['ExtracurricularActivities'].apply(lambda x: 1 if x=='Yes' else 0)

df['PlacementStatus'] = df['PlacementStatus'].apply(lambda x: 1 if x=='Placed' else 0)

target_label = df['PlacementStatus'].values.tolist()
features = df.drop(['StudentID', 'PlacementStatus'],axis = 1).values.tolist()

X_train, X_test, y_train, y_test = train_test_split(features, target_label, test_size=0.2, random_state=42)

# Convert data to PyTorch tensors
#X_train_tensor = torch.FloatTensor(X_train)
#y_train_tensor = torch.FloatTensor(y_train).view(-1, 1)  # Reshape y_train
#X_test_tensor = torch.FloatTensor(X_test)
#y_test_tensor = torch.FloatTensor(y_test).view(-1, 1)  # Reshape y_test

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

pickle.dump(model, open('model.pkl','wb'))