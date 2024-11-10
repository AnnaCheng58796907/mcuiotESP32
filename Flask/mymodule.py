from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    p = f"<p>Hello, Module [{__name__}] !</p>"
    return p

if __name__ == "__main__":
    app.run()