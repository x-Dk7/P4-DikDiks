from flask import Flask, render_template

app = Flask(__name__)


@app.route("/egg")
def egg() :
    return render_template('egg.html')


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/sm64")
def sm64():
    return render_template("sm64.html")


@app.route("/mariosunshine")
def mariosunshine():
    return render_template("mariosunshine.html")


@app.route("/galaxy")
def galaxy():
    return render_template("galaxy.html")


@app.route("/odyssey")
def odyssey():
    return render_template("odyssey.html")


if __name__ == "__main__":
    app.run()
