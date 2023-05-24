# importing flask
from flask import Flask, render_template, request

# importing pickle
import pickle

# Creating our flask project
app = Flask(__name__)
app.secret_key = 'jdada921'

# homepage
@app.route('/')
def index():
    return render_template('submission.html')

# prediction page
# it will take in any numerical value to see what the possible revenue value
# using pickle to "unpickle" our file and pull our linear regression prediction 
@app.route('/prediction', methods = ['POST', 'GET'])
def prediction():
    delaytime = float(request.form['DelayTime'])
    unpickled = pickle.load(open('linearModel-fly.pkl', 'rb'))
    prediction = unpickled.predict([[delaytime]])
    # print(prediction)
    return render_template('prediction.html', prediction = int(prediction[0][0]))

# running our project
if __name__ == '__main__':
    app.run(debug = True)
