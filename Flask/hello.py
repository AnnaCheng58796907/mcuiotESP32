from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, World !</p>"

if __name__ == "__main__":
    app.run()
    #app.run(port=8000)
    #app.run(host='0.0.0.0')
    #app.run(host='0.0.0.0', port=8000)