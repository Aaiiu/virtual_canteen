# Flask主程序入口
# Virtual Canteen Simulation System

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Virtual Canteen System - Coming Soon"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
