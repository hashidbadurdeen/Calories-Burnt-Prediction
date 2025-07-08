from flask import request, Flask, render_template, redirect, session
import mysql.connector
import os
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
app.secret_key = os.urandom(24)

conn = mysql.connector.connect(host="localhost", user="root", password="", database="calories")
cursor = conn.cursor()

model1 = pickle.load(open('Calories.pkl', 'rb'))


def drop(test_df):
    test_df.drop([""], axis=1, inplace=True)
    return test_df


def handle_categorical(test_df):
    Gender_val = 'Gender' + '_' + test_df['Gender'][0]
    if Gender_val in test_df.columns:
        test_df[Gender_val] = 1

    Exercise_Type_val = 'Exercise_Type' + '_' + test_df['Exercise_Type'][0]
    if Exercise_Type_val in test_df.columns:
        test_df[Exercise_Type_val] = 1

    return test_df


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/membership')
def membership():
    return render_template('membership.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/prediction')
def prediction():
    return render_template('prediction.html')


@app.route('/index')
def index():
    if 'id' in session:
        return render_template('index.html')
    else:
        return redirect('/')


@app.route('/login_validation', methods=['POST'])
def login_validation():
    name = request.form.get('name')
    password = request.form.get('password')

    cursor.execute("""SELECT * FROM `user` WHERE `name` LIKE '{}' AND `password` LIKE '{}'"""
                   .format(name, password))
    users = cursor.fetchall()

    if len(users) > 0:
        session['id'] = users[0][0]
        return redirect('/index')
    else:
        return render_template("login.html")


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('username')
    email = request.form.get('useremail')
    password = request.form.get('password')
    gender = request.form.get('gender')
    address = request.form.get('address')
    nic = request.form.get('nic')
    number = request.form.get('number')

    cursor.execute(
        """INSERT INTO `user` (`id`,`name`,`email`,`password`,`gender`,`address`,`nic`,`number`) VALUES(NULL,'{}',
        '{}','{}','{}','{}','{}','{}')""".format(
            name, email, password, gender, address, nic, number))
    conn.commit()

    cursor.execute("""SELECT * FROM `user` WHERE `name` LIKE '{}'""".format(name))
    myuser = cursor.fetchall()
    session['id'] = myuser[0][0]
    return redirect('/login')


@app.route('/add_feedback', methods=['POST'])
def add_feedback():
    username = request.form.get('username')
    email = request.form.get('email')
    feedback = request.form.get('feedback')

    cursor.execute(
        "INSERT INTO `feedback` (`username`, `email`, `feedback`) VALUES (%s, %s, %s)",
        (username, email, feedback)
    )
    conn.commit()

    return redirect('/contact')


@app.route('/predict', methods=['POST'])
def predict():
    print('Applied Machine Learning Course')
    features = request.form
    print(features)
    Gender = features['Gender']
    Age = features['Age']
    Height = features['Height']
    Weight = features['Weight']
    Duration = features['Duration']
    Heart_Rate = features['Heart_Rate']
    Body_Temp = features['Body_Temp']
    Exercise_Type = features['Exercise_Type']

    user_input = {'Gender': [Gender], 'Age': [Age], 'Height': [Height], 'Weight': [Weight], 'Duration': [Duration],
                  'Heart_Rate': [Heart_Rate],
                  'Body_Temp': [Body_Temp], 'Exercise_Type': [Exercise_Type]}
    test_df = pd.DataFrame(user_input)

    new_df = pd.DataFrame(np.zeros(shape=(1, 4)).astype(int), columns=(['male', 'female', 'Cardio', 'Machine']))

    test_df = pd.concat([test_df], axis=1)

    test_df = handle_categorical(test_df)

    print(test_df)

    prediction = model1.predict(test_df)

    output = float(np.round(prediction[0], 2))

    print(output)

    return render_template('result.html', prediction_text='Your Calorie Burnt is {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
