from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('flasky.cfg')

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

if __name__ == "__main__":
  app.run()