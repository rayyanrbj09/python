from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html><h1>Hello, World!</h1></html>"

@app.route('/index')
def index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)