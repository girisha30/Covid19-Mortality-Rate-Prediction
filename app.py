import pickle
import numpy
from flask import Flask, request, render_template
import pandas as pd
#Global variables

app = Flask(__name__)
loadedModel = pickle.load(open('Covid-19_India_Status.pkl','rb'))

#User Defined functions
@app.route("/", methods = ['GET'])
def Home():
    return render_template('index.html')

#user input commands
@app.route('/prediction',methods=['POST'])
def predict():
    State=request.form['State']
    TotalCases=int(request.form['TotalCases'])
    Active=int(request.form['Active'])
    Discharged=int(request.form['Discharged'])

    prediction=loadedModel.predict(pd.DataFrame(data=[(State,TotalCases,Active,Discharged)],columns=['State/UTs','Total Cases','Active','Discharged']))[0]

    return render_template('index.html',covid_deaths_output = prediction)

#main function
if __name__=="__main__":
     app.run(debug=True)
