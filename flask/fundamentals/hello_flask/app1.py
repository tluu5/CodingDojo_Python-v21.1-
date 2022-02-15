from flask import Flask, hello_flask
app = Flask(__name__)
@app.route('/')
def index():
    return hello_flask('app1_index.html')
if __name__ == "__main__":
    app.run(debug=True)