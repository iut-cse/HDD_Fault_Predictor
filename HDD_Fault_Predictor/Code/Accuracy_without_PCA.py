import pandas as pd
from sklearn.naive_bayes import GaussianNB
import classification as clf_2
def without_pca():
    df=pd.read_csv('../Data/Final.csv')
    del df['serial_number']
    del df['Unnamed: 0']
    del df['dt']
    del df['manufacturer']

    X = df.iloc[:, 0:-1]
    y = df.iloc[:, -1]
    clf=GaussianNB()
    clf.fit(X,y)
    print('Accuracy without PCA: ')
    print('Naive Bayes:         ',clf.score(X,y)*100,' %')
    print('Logistic Regression: ',clf_2.classify(X,y)*100,' %')


without_pca()


