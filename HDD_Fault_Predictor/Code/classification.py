from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def classify(x, y):
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.40, random_state=40)
    clf = LogisticRegression(solver='lbfgs', class_weight='balanced', max_iter=10000)
    clf.fit(X_train, y_train)
    prediction = clf.predict(X_test)
    acr = accuracy_score(y_test, prediction)
    return acr