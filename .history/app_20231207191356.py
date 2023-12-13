from flask import Flask, render_template, url_for, request


app=Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')  

@app.route('/home')
def home():
    return render_template('home.html')    

@app.route('/login', methods=['GET','POST'])
def login():
    return 

if __name__=='__main__':
    app.run(debug=True)