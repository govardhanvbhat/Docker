from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to DevOps!</h1>"

@app.route('/about')
def about():
    return "<h1>Welcome to About page</h1>"

@app.route('/contact')
def contact():
    return "<h1 style=\"color:yellow\">Contact!</h1>"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)