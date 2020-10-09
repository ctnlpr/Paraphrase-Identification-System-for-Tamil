# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:27:03 2018

@author: Sankaralingam
"""
import featurizer
from sklearn.externals import joblib
from flask import Flask, render_template, request
app = Flask(__name__)

tdm_vocabulary = joblib.load('../Models/tdm_vocabulary.pkl')
tdm_model = joblib.load('../Models/tdm_model.pkl')

tfidf_vocabulary = joblib.load('../Models/tfidf_vocabulary.pkl')
tfidf_model = joblib.load('../Models/tfidf_model.pkl')

##sentence1 = 'நான் என்ற சொல்லை ஒழிப்பதன்மூலம் நாம் என்ற ஒற்றுமையை உருவாக்கிடுவோம் .'
##sentence2 = 'நான் என்ற சொல்லை ஒழித்து நாம் என்று உருவாக்குவோம் .'

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

       
@app.route('/')
def student():
   return render_template('student.html')

@app.route('/resul',methods = ['POST', 'GET'])
def resul():
    if request.method == 'POST':
        sentence1 = request.form['textarea1']
        sentence2 = request.form['textarea2']
        print sentence1
        TEST = request.form['radioButton']
        name = sentence1, sentence2, TEST
        sentence1, sentence2, TEST = name.split('||')
        result = get_class(sentence1, sentence2, TEST)
        print result
        if result > 0.9:
            print result
            resul = "Para-Phrase"
            resul = request.form
        elif result < 0.5:
            print result
            resul = "not a Para-Phrase"
            resul = request.form
        else:
            print result
            resul = "semi Para-Phrase"
            resul = request.form
    return render_template("resul.html",resul = resul)

if __name__ == '__main__':
   app.run(host='localhost')