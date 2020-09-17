import pandas as pd
from sklearn.naive_bayes import GaussianNB
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
    print('Accuracy without PCA: ',clf.score(X,y))


without_pca()


