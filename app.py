from logging import debug
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:password@localhost:3306/login'
db=SQLAlchemy(app)

class Logs(db.Model):
    sno=db.Column(db.Integer,primary_key=True,autoincrement=True)
    email=db.Column(db.String(20),nullable=False)
    password=db.Column(db.String(20))
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['pwd']
        entry=Logs(email=email,password=password)
        db.session.add(entry)
        db.session.commit()
        return "Login successful"

    return render_template('login.html')

if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)
