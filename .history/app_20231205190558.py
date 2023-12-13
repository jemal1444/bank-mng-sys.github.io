from flask import Flask, render_template,url_for

app=Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

if ___name___=='__main__':
    app.run(debug=True)