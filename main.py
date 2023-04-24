from re import template
from flask import Flask,render_template,request
import pickle 
# {{ url_for('static',filename='home.css')}}
app=Flask(__name__)


file=open('model.pkl','rb')
clf=pickle.load(file)
file.close()

@app.route('/') 
def home():
    return render_template("home.html")


@app.route('/know_more')
def know_more():
    return render_template("know_more.html")


@app.route("/analytics")
def analytic():
    return render_template("analytics.html")

@app.route("/genderwise")
def topvacinated():
    return render_template("Top Vaccinated states.html")
@app.route("/topactive")
def totalactive():
    return render_template("Total Active Cases.html")
@app.route("/totalconfirmed")
def totalconfirmed():
    return render_template("Total Confirmed.html")
@app.route("/totaldeath")
def totaldeaths():
    return render_template("Total Deaths.html")
@app.route("/confirmedvedeaths")
def confirmedvsdeath():
    return render_template("confirmed cases vs Deaths.html")



@app.route('/probabilitydetector',methods=["GET","POST"])
def covid_prob_dect():
    if request.method=="POST":
        mydict=request.form
        fever=int(mydict['fever'])
        age=int(mydict['age'])
        bodypain=int(mydict['bodypain'])
        loss=int(mydict['loss-taste-smell'])
        soreThroat=int(mydict['soreThroat'])
        headache=int(mydict['head-ache'])
        diffbreathing=int(mydict['diff-breathing'])
# Fever	Body Pain	Age	Lost of smell or taste	Sore throat	headache	Difficulty in breathing
        inputFeatures=[fever,bodypain,age,loss,soreThroat,headache,diffbreathing]
        infprob=clf.predict_proba([inputFeatures])[0][1]
        print(infprob)
        return render_template("show.html",infprob=round(infprob*100))

    return render_template("index.html")



if __name__=="__main__":
    app.run(debug=True,port=5000)
