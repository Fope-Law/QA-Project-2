from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    
    yinyang = requests.get('http://fortune-gem:2020/yin_yang')
    gems = requests.get('http://fortune-gem:2020/gem_stone')
    fortune = requests.post('http://fortune-gem:2020/get_fortune', data=yinyang.text,gems.text)
    return render_template('index.html', yinyang=yinyang.text, gem_stone=gem_stone.text, fortune=fortune.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2020, debug=True)
