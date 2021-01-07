from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Mario Museum!"
    <iframe src="https://drive.google.com/file/d/1YzrzgJ5fCn_RSHAH9E8uOjajw0BCb1uS/preview" width="640" height="480"></iframe>

if __name__ == "__main__":
    app.run()
