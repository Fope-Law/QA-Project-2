from flask import Flask, request
import requests, random

app = Flask(__name__)

@app.route('/yin_yang', methods=['GET'])
def yin_yang():
    return random.choice(['yin', 'yang'])

@app.route('/get_fortune', methods=['POST'])
def get_fortune():
    
    fortunes = {"yin":["You will receive good news in the next few days.", "Your shower singing will take you to great heights.", "You will learn to cook an amazing meal this month.", "People will criticise you for trying but you will learn a new skill this month."], 
    "yang":["You will have to work overtime soon...", "Your socks will not match for the next week...", "You will not get enough sleep this Saturday...","You will be labelled a fool in your time of greatest need..."]}
    
    return random.choice(fortunes[request.data.decode('utf-8')])

@app.route('/get_gem', methods=['POST'])
def get_gem():
    
    gems = {"yin":["Amazonite", "Amber", "Citrine", "Jade", "Onyx", "Rose Quartz"], 
    "yang":["Amethyst", "Andalusite", "Pearl", "Nephrite", "Sapphire", "Topaz"]}
    
    return random.choice(gems[request.data.decode('utf-8')])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2020, debug=True)
