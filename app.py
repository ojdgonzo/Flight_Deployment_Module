from flask import Flask, render_template, request

# importing pickle
import pickle


app = Flask(__name__)
app.secret_key = 'jdada921'

@app.route('/')
def index():
    return render_template('submission.html')


@app.route('/prediction', methods = ['POST', 'GET'])
def prediction():
    delaytime = float(request.form['DelayTime'])
    unpickled = pickle.load(open('linearModel-fly.pkl', 'rb'))
    prediction = unpickled.predict([[delaytime]])
    # print(prediction)
    return render_template('prediction.html', prediction = int(prediction[0][0]))

if __name__ == '__main__':
    app.run(debug = True)
