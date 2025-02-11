from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/yes")
def yes():
    return "<h1>Thanks for Accepting!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
