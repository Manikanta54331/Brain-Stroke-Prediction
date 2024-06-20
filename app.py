from flask import Flask,render_template,request
import numpy as np
import sklearn
import pickle
import pandas as pd

app=Flask(__name__)

@app.route('/')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template("register.html")

@app.route('/signin')
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about", methods=['GET'])
def about():    
    return render_template("about.html")

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/bmi')
def bmi():
    return render_template('bmi.html')


@app.route('/result', methods=['POST'])
def predictAction():
    if request.method == 'POST':


        age = request.form['age']
        maritalstatus = request.form['ever_married']
        worktype = request.form['work_type']
        residence = request.form['Residence_type']
        gender = request.form['gender']
        bmi = request.form['bmi']
        gluclevel = request.form['avg_glucose_level']
        smoke = request.form['smoking_status']
        hypertension = request.form['hypertension']
        heartdisease = request.form['heart_disease']
        #model = pickle.load(open('stroke_new.pkl','wb'))

        res={'urban':1,'rural':0}
        gen={'Female':0,'Male':1}
        msts={'married':1,'not married':0}
        wktype={'privatejob':2,'govtemp':1,'selfemp':3}
        smke={'formerly-smoked':1,'non-smoker':2,'smoker':3}
        hypten={'hypten':1,'nohypten':0}
        hrtdis={'heartdis':1,'noheartdis':0}




        model=pd.read_pickle('strokenew.pkl')

        array = [[gender,age,hypertension,heartdisease,maritalstatus,worktype,residence,gluclevel,bmi,smoke]]


        array = [np.array(array[0],dtype = 'float64')]
        pred_stroke = model.predict(array)
        result = int(pred_stroke[0])
        if result==1:
            return render_template('stroke.html')
        else:
            return render_template('nostroke.html')

@app.route('/counsel')
def counsel():
    return render_template('counsel.html')

if __name__=="__main__":
    app.run(debug=True,port=5000)