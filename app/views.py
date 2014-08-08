from app import flask_app
from flask import render_template
from models import Game, Function
import json

@flask_app.route("/", methods = ["GET"])
@flask_app.route("/home", methods = ["GET"])
def home():
    game = Game()
    data = json.dumps(game.data)
    game_id = json.dumps(game.game_id)
    print 'game_id {0}'.format(game_id)
    print 'forumla {0}'.format(game.function.formula)
    return render_template("home.html", data=data, game_id=game_id)

@flask_app.route("/answer/<question_id>/<guess>", methods = ["GET"])
def answer(question_id, guess):
    users_function = Function.new_from_function(guess)
    current_game = Game.get(int(question_id))
    if current_game.function.is_equal(users_function):
        print 'correct answer'
        #new_game = Game()

    guess = json.dumps(users_function.data)
    question = json.dumps(current_game.data)
    return json.dumps({'question': question, 'guess': guess})
