from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('KNNModel.pkl','rb'))

app = Flask(__name__)


@app.route('/')
def man():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    arr = [[5.6,3.0]]
    p = model.predict(arr)
    print("Class: ",p," value: ",p[0])
    return render_template('after.html',data = p[0])

if __name__ == "__main__":
    app.run(debug=True)