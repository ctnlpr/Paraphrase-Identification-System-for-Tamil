

def get_dtm(trainPair1, trainPair2, testPair1, testPair2, trainLabels, testLabels):
    import classifier
    import featurizer
    from sklearn.feature_extraction.text import CountVectorizer
    final_f1 = 0
    for n_gram in range(1,11):
        for mini_df in range(1, 6):
            tf_vectorizer = CountVectorizer(min_df=mini_df, ngram_range=(1, n_gram))
            tf_vectorizer.fit(list(trainPair1) + list(trainPair2))
            trainPair1_Mat = tf_vectorizer.transform(list(trainPair1)).todense()
            trainPair2_Mat = tf_vectorizer.transform(list(trainPair2)).todense()
            testPair1_Mat = tf_vectorizer.transform(list(testPair1)).todense()
            testPair2_Mat = tf_vectorizer.transform(list(testPair2)).todense()
            trainFeat = featurizer.get_features(trainPair1_Mat, trainPair2_Mat)
            testFeat = featurizer.get_features(testPair1_Mat, testPair2_Mat)
            f1, model = classifier.get_classification(trainFeat, trainLabels, testFeat, testLabels)
            if f1 > final_f1:
                final_f1 = f1
                final_n_gram = n_gram
                final_mini_df = mini_df

    tf_vectorizer = CountVectorizer(min_df=final_mini_df, ngram_range=(1, final_n_gram))
    tf_vectorizer.fit(list(trainPair1) + list(trainPair2))
    trainPair1_Mat = tf_vectorizer.transform(list(trainPair1)).todense()
    trainPair2_Mat = tf_vectorizer.transform(list(trainPair2)).todense()
    testPair1_Mat = tf_vectorizer.transform(list(testPair1)).todense()
    testPair2_Mat = tf_vectorizer.transform(list(testPair2)).todense()
    trainFeat = featurizer.get_features(trainPair1_Mat, trainPair2_Mat)
    testFeat = featurizer.get_features(testPair1_Mat, testPair2_Mat)
    f1, model = classifier.get_classification(trainFeat, trainLabels, testFeat, testLabels)
    print('tdm + SVM with linear kernel trained with f1 score: ', f1)
    return tf_vectorizer, model


def get_tfidf(trainPair1, trainPair2, testPair1, testPair2, trainLabels, testLabels):
    import classifier
    import featurizer
    from sklearn.feature_extraction.text import TfidfVectorizer
    final_f1 = 0
    for n_gram in range(1,11):
        for mini_df in range(1, 6):
            tf_vectorizer = TfidfVectorizer(min_df=mini_df, ngram_range=(1, n_gram))
            tf_vectorizer.fit(list(trainPair1) + list(trainPair2))
            trainPair1_Mat = tf_vectorizer.transform(list(trainPair1)).todense()
            trainPair2_Mat = tf_vectorizer.transform(list(trainPair2)).todense()
            testPair1_Mat = tf_vectorizer.transform(list(testPair1)).todense()
            testPair2_Mat = tf_vectorizer.transform(list(testPair2)).todense()
            trainFeat = featurizer.get_features(trainPair1_Mat, trainPair2_Mat)
            testFeat = featurizer.get_features(testPair1_Mat, testPair2_Mat)
            f1, model = classifier.get_classification(trainFeat, trainLabels, testFeat, testLabels)
            if f1 > final_f1:
                final_f1 = f1
                final_n_gram = n_gram
                final_mini_df = mini_df

    tf_vectorizer = TfidfVectorizer(min_df=final_mini_df, ngram_range=(1, final_n_gram))
    tf_vectorizer.fit(list(trainPair1) + list(trainPair2))
    trainPair1_Mat = tf_vectorizer.transform(list(trainPair1)).todense()
    trainPair2_Mat = tf_vectorizer.transform(list(trainPair2)).todense()
    testPair1_Mat = tf_vectorizer.transform(list(testPair1)).todense()
    testPair2_Mat = tf_vectorizer.transform(list(testPair2)).todense()
    trainFeat = featurizer.get_features(trainPair1_Mat, trainPair2_Mat)
    testFeat = featurizer.get_features(testPair1_Mat, testPair2_Mat)
    f1, model = classifier.get_classification(trainFeat, trainLabels, testFeat, testLabels)
    print('tfidf + SVM with linear kernel trained with f1 score: ', f1)
    return tf_vectorizer, model
