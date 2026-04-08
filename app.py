from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to DevOps System Monitor!"

@app.route('/metrics')
def metrics():
    return jsonify({
    "cpu_percent": psutil.cpu_percent(interval=1),
    "memory": psutil.virtual_memory()._asdict(),
    "disk": psutil.disk_usage('/')._asdict()
})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)