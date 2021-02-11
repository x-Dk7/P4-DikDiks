from flask import Flask, render_template

app = Flask(__name__)

@app.route("/game")
def game():
    return render_template('mini-game.html')

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/sm64")
def sm64():
    return render_template("sm64.html")

@app.route("/sunshine")
def sunshine():
    return render_template("mariosunshine.html")

@app.route("/galaxy")
def galaxy():
    return render_template("galaxy.html")

@app.route("/odyssey")
def odyssey():
    return render_template("odyssey.html")

@app.route("/egg")
def egg() :
    return render_template('egg.html')

if __name__ == "__main__":
    app.run(debug = True)
