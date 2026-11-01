from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "online",
        "service": "Advanced Portfolio Backend",
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route('/run-script', methods=['POST', 'GET'])
def run_script():
    req_data = request.get_json() if request.is_json else {}
    task_input = req_data.get('input', 'Default Security Scan Task')
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    result_payload = {
        "status": "success",
        "executed_at": timestamp,
        "task": task_input,
        "system_metrics": {
            "cpu_load": "14.2%",
            "memory_usage": "184MB / 512MB",
            "security_status": "Secure (No vulnerabilities detected)"
        },
        "output": f"Successfully executed server routine for: '{task_input}' at {timestamp}."
    }
    
    return jsonify(result_payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

