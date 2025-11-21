from flask import Flask
'''
 Creates a instance of flask i.e
 Web Server Gateway Interface
'''
# WSGI APPLICATION
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome Welcome one all"
@app.route('/index')
def indexPage():
    return "Welcome to this index page"

if(__name__=="__main__"):
    app.run(debug=True)