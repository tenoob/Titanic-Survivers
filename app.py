
from flask import Flask,render_template,request
import pickle



app = Flask(__name__)
model = pickle.load(open('DecisionTree.pkl','rb'))

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def prediction():
    if (request.method=='POST'):
        Pclass = int(request.form['Pclass'])
        age =  int(request.form['age'])
        SibSp = int(request.form['SibSp'])
        Parch = int(request.form['parch'])
        gender = int(request.form['gender'])
        embark = request.form['embark']
        
        print(Pclass ,age , SibSp, Parch , gender ,embark)
        
        predictors = [Pclass,age,SibSp,Parch,gender]
        if embark=='Q':
            predictors.extend([1,0])
        elif embark=='S':
            predictors.extend([0,1])
        else:
            predictors.extend([0,0])

        #print(predictors)
        result = model.predict([predictors])

        if result[0]==1:
            ans = "Survived"
        else:
            ans='Not Survived'
        return render_template('index.html',result=ans)

if __name__=='__main__':
    app.run(debug=True)