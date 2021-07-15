from flask import flask
import random

app = Flask(__name__)

@app.route('/gem_stone' methods=['GET'])
def gem_stone():
    return random.choice(['yin', 'yang'])

@app.route('/get_fortune', methods=['POST'])
def get_fortune():
    
    gems = 
    
    {"yin":["Amazonite", "Amber", "Citrine", "Jade", "Onyx", "Rose Quartz"], 
    "yang":["Amethyst", "Andalusite", "Pearl", "Nephrite", "Sapphire", "Topaz"]}
    
    return fortunes[request.data.decode('utf-8')]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2020, debug=True)
