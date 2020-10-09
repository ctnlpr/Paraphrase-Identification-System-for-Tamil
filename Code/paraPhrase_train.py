import config
import load_data
import representation
from sklearn.externals import joblib


# getting path
trainFile = config.trainFilePath
trainLabel = config.trainLabels
testFile = config.testFilePath
testLabel = config.testLabels

# getting data
trainPair1, trainPair2, trainLabels = load_data.get_data(trainFile,trainLabel)
testPair1, testPair2, testLabels = load_data.get_data(testFile,testLabel)

##TRAIN = 'DTM'
# representation
##if TRAIN == 'DTM':
tdm_vocabulary, tdm_model = representation.get_dtm\
                            (trainPair1, trainPair2, testPair1, testPair2, trainLabels, testLabels)
joblib.dump(tdm_vocabulary, '../Models/tdm_vocabulary.pkl')
joblib.dump(tdm_model, '../Models/tdm_model.pkl')
    
##elif TRAIN == 'TFIDF':
tfidf_vocabulary, tfidf_model = representation.get_tfidf\
                            (trainPair1, trainPair2, testPair1, testPair2, trainLabels, testLabels)
joblib.dump(tfidf_vocabulary, '../Models/tfidf_vocabulary.pkl')
joblib.dump(tfidf_model, '../Models/tfidf_model.pkl')


