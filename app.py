from flask import Flask

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")


@app.route("/")
def index():
    return "<h1>Hallo Travis CI</h1>"


if __name__ == "__main__":
    app.run()
