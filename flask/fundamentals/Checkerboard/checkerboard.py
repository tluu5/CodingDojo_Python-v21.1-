from distutils.log import debug
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
print(__name__)
@app.route('/')
def index():
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)