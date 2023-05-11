from flask import Flask

facebook = Flask(__name__)

@facebook.route("/")
def index():
    return index


@facebook.route("/about")
def about():
    return "<h1>Сайт</h1>"


if __name__ == "__main__":
    facebook.run(debug=True)