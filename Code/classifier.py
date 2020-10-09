

def get_classification(trainFeat, trainLabel, testFeat, testLabel):
    from sklearn import svm
    from sklearn.metrics import f1_score
    clf = svm.SVC(kernel='linear', C=1, probability=True).fit(trainFeat, trainLabel)
    prediction = clf.predict(testFeat)
    f1 = f1_score(testLabel, prediction)
    return f1, clf
