import random
import json
from flask import Flask, send_file, jsonify, request

app = Flask(__name__)

# Carichiamo il file JSON dei giocatori (esempio con 10 giocatori NBA)
with open('players.json') as f:
    players_data = json.load(f)

@app.route("/")
def index():
    return "Benvenuto nell'API dei giocatori NBA!"

# Route per scaricare il file JSON completo
@app.route("/players")
def all_players():
    # Restituisce il file JSON completo
    return jsonify(players_data)

# Route per un giocatore casuale
@app.route("/random")
def random_player():
    # Restituisce un giocatore scelto a caso
    player = random.choice(players_data)
    return jsonify(player)

if __name__ == "__main__":
    app.run(debug=True)
