
import flask, os, json
from flask import render_template, jsonify, Flask

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
	return flask.render_template('home.html')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(debug=True, host='0.0.0.0', port=port)