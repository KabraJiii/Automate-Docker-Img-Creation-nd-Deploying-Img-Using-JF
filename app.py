from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Piyush Kabra"

@app.route('/status')
def status():
    return {"status": "App is Also running successfully"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
