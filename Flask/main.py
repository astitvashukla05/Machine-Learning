from flask import Flask,render_template,request
'''
 Creates a instance of flask i.e
 Web Server Gateway Interface
'''
# WSGI APPLICATION
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask testing</h1></html>"

@app.route('/index',methods=['get'])
def indexPage():
    return render_template('index.html')

@app.route('/formPage',methods=['GET','POST'])
def formPage():
    if(request.method=='POST'):
        name=request.form['name']
        passw=request.form['pass']
        check=request.form['check']
        return render_template(
            'submit.html', 
            name=name,
            passw=passw,
            check=check)
    return render_template('form.html')

# app.route('/submit',methods=['GET','POST'])
# def getInfo():
#     if(request.method=='POST'):
#         render_template('submit.html')

# Variable Rule
@app.route('/sucess/<int:score>')
def success(score):
    return f"The marks you got is {score}"
if(__name__=="__main__"):
    app.run(debug=True) 