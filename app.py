from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
@app.route('/')
def home():
  return 'Hello, Continuous Deployment!'
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001)

metrics = PrometheusMetrics(app)
metrics.info("app_info", "Application Info", version="1.0.0")