import os

from flask import Flask, render_template, redirect, request

app = Flask(__name__)


def write_player_name(file, name):
    with open(file, "a") as player_list:
        player_list.writelines(name)


@app.route('/', methods=["GET", "POST"])
def index():
    """Start page with instructions and user name submission"""
    if request.method == "POST":
        write_player_name("data/players_names.txt", request.form["player_name"] + "\n")
        return redirect(request.form["player_name"])
    return render_template("index.html")

@app.route('/<player_name>', methods=["GET", "POST"])
def load(player_name):
    return render_template("quiz.html", player_name=player_name)
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(os.environ.get('PORT', 0)), debug=True)