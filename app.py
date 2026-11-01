from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "Backend is running successfully!"})

@app.route('/run-script', methods=['GET', 'POST'])
def run_script():
    # You can put your custom Python logic here later!
    script_output = "Hello from your deployed Python backend server!"
    return jsonify({"output": script_output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
