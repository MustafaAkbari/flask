from flask import Flask

app = Flask(__name__)

# basic routing


@app.route('/')
def home():
    return "<h1>Go to 'names/name' to see changing your name</h1>"

# dynamic routing


@app.route("/names/<name>")
def changing_names(name):
    if " " in name:
        name = name.replace(" ", "_")
    elif name[-1] != "y":
        name = name + "y"
    elif name[-1] == "y" and "y" not in name[0:-1]:
        name = name.replace(name[-1], "iful")
    return f"<h1>you name changed to {name}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
