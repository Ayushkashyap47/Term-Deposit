from flask import Flask, render_template, request
from flask_cors import CORS,cross_origin
import pickle
import numpy as np

model = pickle.load(open('final_model3.pickle', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def home():
        data1 = request.form['Job']
        data2 = request.form['Marital_Status']
        data3 = request.form['Education']
        data4 = request.form['default']
        data5 = request.form['Housing']
        data6 = request.form['Loan']
        data7 = request.form['contact']
        data8 = request.form['month']
        data9 = request.form['day_of_week']
        data10 = request.form['duration']
        data11 = request.form['campaign']
        # arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11]], dtype='float64')
        pred = model.predict([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11]])

        return render_template('after.html', data=pred[0])

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=7001, debug=True)


