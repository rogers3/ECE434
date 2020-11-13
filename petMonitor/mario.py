#!/usr/bin/env python3

from flask import Flask,render_template,request
 
app = Flask(__name__)
 
@app.route('/form')
def form():
    return render_template('hello.html')
 
@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        print(form_data)
        return render_template('hello.html',form_data = form_data)
 
 
if __name__ == "__main__":
   app.run(debug=True, port=434, host='0.0.0.0')