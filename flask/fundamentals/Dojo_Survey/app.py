from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    title = "Thieu Luu's Blog"
    return render_template("index.html", title = title)
@app.route('/about')
def about():
    title = "About Thieu Luu"
    names = ["John", "Mary", "Wes", "Sally"]
    return render_template("about.html", names = names, title = title)