from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World'


@app.route('/name/<name>')
def name_site(name):
	return name;
@app.route('/post/<int:post_id>') # 타입 제어
def show_post(post_id):
	return 'Post %d' %post_id





if __name__=='__main__':
	app.debug = True
	app.run()
