from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/hello/<string:banana>/<int:num>')
def hello(banana,num):
    return render_template("hello.html",banana=banana,num = num)
@app.route('/lists')
def render_lists():
    users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template("lists.html", random_numbers = [3,1,5], users = users)
if __name__ == "__main__":
    app.run(debug=True)