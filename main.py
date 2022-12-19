from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")  # whenever / is inserted in the URL it will lead to the homepage
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
