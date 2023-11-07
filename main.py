from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
