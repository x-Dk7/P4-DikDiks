from flask import Flask, render_template

app = Flask(__name__)


@app.route("/mini-game")
def mini-game() :
    return render_template('mini-game.html')

if __name__ == "__main__":
    app.run()
