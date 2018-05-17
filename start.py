from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html", title = 'Index')

@app.route('/grupo01')
def grupo01():
	return render_template('grupo01/page.html')