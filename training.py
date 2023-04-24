import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

df=pd.read_csv('data.csv')
def data_split(data,ratio):
    np.random.seed(42)
    shuffuled=np.random.permutation(len(data))
    test_set_size=int(len(data)*ratio)
    test_indices=shuffuled[:test_set_size]
    train_indices=shuffuled[test_set_size:]
    return data.iloc[train_indices],data.iloc[test_indices]
train,test=data_split(df,0.2)
X_train=train[['Fever','Body Pain','Age','Lost of smell or taste','Sore throat','headache','Difficulty in breathing']]
X_test=test[['Fever','Body Pain','Age','Lost of smell or taste','Sore throat','headache','Difficulty in breathing']]
X_train.to_numpy()
Y_train=train[['Infection probability']].to_numpy().reshape(276 ,)
Y_test=test[['Infection probability']].to_numpy().reshape(68,)
clf=LogisticRegression()
clf.fit(X_train,Y_train)
infprob=clf.predict_proba([[100,1,22,1,1,0,1,1]])[0][1]







