from flask import Flask

def create_app():
	"""docstring for create_app"""
	app = Flask(__name__)
	@app.route("/")
	def home():
		"""docstring for home"""
		return "IT WORKS"
	return app