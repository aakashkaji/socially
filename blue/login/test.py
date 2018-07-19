
# This file is used as example purpose

from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
	return "Hello World !! fddddddddd"

@app.route('/home')
def home():
	return "<body><marquee> hello aakash gupta python  </marquee></body>"




#start apps here

#app.run(debug=True)