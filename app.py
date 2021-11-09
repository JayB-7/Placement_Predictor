import flask
from flask import render_template, request
import pickle

app = flask.Flask(__name__)
filename = 'model.pkl'
classifier = pickle.load(open(filename, 'rb'))


@app.route('/')
def Home():
    return render_template('index.html')


@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        Score = int(request.form['score'])
        Apti = int(request.form['aptitude'])
        Eng = int(request.form['english'])
        Quant = int(request.form['quantitative'])
        Anly = int(request.form['analytical'])
        Dom = int(request.form['domain'])
        CF = int(request.form['compfund'])
        Code = int(request.form['coding'])
        prediction = classifier.predict([[Score, Apti, Eng, Quant, Anly, Dom, CF, Code]])
        output = int(prediction[0])
        if output == 0:
            return render_template('index.html', prediction_text ="Sorry this student will not be placed")
        else:
            return render_template('index.html', prediction_text ="Yaay, this student will be placed")
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
