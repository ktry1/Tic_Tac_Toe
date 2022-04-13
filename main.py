from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def choice():
    return render_template("choice.html")

@app.route("/Pvp")
def play_pvp():
    return render_template("player_v_player.html")

@app.route("/Ai")
def play_ai():
    return render_template("player_vs_ai.html")


if __name__ == "__main__":
    app.run()