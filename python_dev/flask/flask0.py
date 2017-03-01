from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return "This is the index page. \nEat a large dick, sir."

@app.route('/hello')
def hello():
	return "Oh hello there. "

@app.route('/about')
def about():
	return "My first Flask App"

@app.route('/projects/')
def projects():
	return 'Project Page'

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' %username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post ID %d' %post_id