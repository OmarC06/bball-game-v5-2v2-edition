from flask import Flask, request, jsonify
from flask_cors import CORS  # import CORS\
from gameLogic import *

app = Flask(__name__)
CORS(app)

u1 = Player("1", "Guard")
u2 = Player("2", "Big")   

c1 = Player("1", "Guard")
c2 = Player("2", "Big")

fullGame = Game(u1, u2, c1, c2, "Easy")
print(fullGame.score)
fullGame.startGame()

@app.route("/options", methods=['GET'])
def showOptions():
    return jsonify(fullGame.getOptions())

@app.route("/confirm", method=["POST"])
def receiveOption():
    pass

if __name__ == "__main__":
    app.run(debug=True)