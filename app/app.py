from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Prometheus metrics
metrics = PrometheusMetrics(app)

# Basic application information
metrics.info(
    "cloud_devops_platform",
    "Cloud DevOps Platform Application",
    version="1.0.0"
)


@app.route("/")
def home():
    return "Cloud DevOps Platform Running"


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/ready")
def ready():
    return jsonify({
        "status": "ready"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)