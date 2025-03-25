# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5


# create an instance of Flask
app = Flask(__name__)

# route decorator binds a function to a URL
@app.route('/')
def hello():
  return '<p>Thomas : afk<p><p>Jacob : who<p>'

@app.route('/jacob')
def t_test():
   return render_template('template.html')

bootstrap = Bootstrap5(app)

# https://github.com/JZmor/cst205-lab15