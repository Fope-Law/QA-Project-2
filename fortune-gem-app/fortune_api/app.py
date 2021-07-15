from flask import flask
import random

app = Flask(__name__)

@app.route('/yin_yang' methods=['GET'])
def yin_yang():
    return random.choice(['yin', 'yang'])

@app.route('/get_fortune', methods=['POST'])
def get_fortune():
    
    fortunes = 
    
    {"yin":["You will receive good news in the next few days.", "You will lean to cook an amazing meal this month."], 
    "yang":["You will have to work overtime soon.", "Your socks will not match for the next week.","You will not get enough sleep this Saturday."]}
    
    return fortunes[request.data.decode('utf-8')]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2020, debug=True)
