from bottle import Bottle, template, request
import featurizer
from sklearn.externals import joblib
from bottle import route, run, template


tdm_vocabulary = joblib.load('../Models/tdm_vocabulary.pkl')
tdm_model = joblib.load('../Models/tdm_model.pkl')

tfidf_vocabulary = joblib.load('../Models/tfidf_vocabulary.pkl')
tfidf_model = joblib.load('../Models/tfidf_model.pkl')

def get_class(sentence1, sentence2, TEST):
    if TEST == 'DTM':
        test1 = tdm_vocabulary.transform([sentence1]).todense()
        test2 = tdm_vocabulary.transform([sentence2]).todense()
        testFeat = featurizer.get_features(test1, test2)
        result = (tdm_model. predict_proba(testFeat))[0][1]
    elif TEST == 'TFIDF':
        test1 = tfidf_vocabulary.transform([sentence1]).todense()
        test2 = tfidf_vocabulary.transform([sentence2]).todense()
        testFeat = featurizer.get_features(test1, test2)
        result = (tfidf_model. predict_proba(testFeat))[0][1]
    else:
        result = 'choose a correct representation method'
    return result


app = Bottle()

@app.route('/')
def index():
    """Home Page"""
    
    return template("form.tpl", info="",inf="",st="",stm="") 

@app.route('/', method="POST")
def formhandler():
    """Handle the form submission"""
    
    first = request.forms.get('first')
    last = request.forms.get('last')
    TEST = request.forms.get('radioButton')
    result = get_class(first, last, TEST)
    if result > 0.9:
        print(result)
        result1 = "Para-Phrase"
    elif result < 0.5:
        print(result)
        result1 = "not a Para-Phrase"
    else:
        print(result)
        result1 = "semi Para-Phrase"
    #message = "Hello " + result1 + "\n" + last + "."
    info = first
    inf = last
    st = result1
    stm = result
    
    #message = info
    
    return template("form.tpl", info=info,inf=inf,st=st,stm=stm) 

if __name__ == '__main__':
    app.run(host='localhost',port=9807)