from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    
    yinyang = requests.get('http://yinyang_api:2020/yin_yang')
    fortune = requests.post('http://yinyang_api:2020/get_fortune', data=yinyang.text)
    gem = requests.post('http://yinyang_api:2020/get_gem', data=yinyang.text)
    return render_template('index.html', fortune=fortune.text, gem=gem.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2020, debug=True)
