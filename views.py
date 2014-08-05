from app import flask_app
from flask import render_template
from models import *
import json

@flask_app.route("/", methods = ["GET"])
@flask_app.route("/home", methods = ["GET"])
def home():
    game = Game()
    data = json.dumps(game.data)
    game_id = json.dumps(game.game_id)
    return render_template("home.html", data=data, game_id=game_id)

@flask_app.route("/answer/<question_id>/<guess>", methods = ["GET"])
def answer(question_id, guess):
    function = Function(guess)
    guess = json.dumps(function.data)
    question = json.dumps(Game.get(int(question_id)).data)
    return json.dumps({'question': question, 'guess': guess})
