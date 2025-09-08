from flask import Flask
from datetime import datetime
import time
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Simulate CPU work
    start_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    start_at_val = datetime.now()
    x = 0
    # for _ in range(10_000_000):
    # for _ in range(1_000_000):
    #     x += 1
    # time.sleep(2)  # 2 sec delay
    end_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    end_at_val = datetime.now()
    duration = (end_at_val - start_at_val).total_seconds()
    # return "OK"  
    return {
      "status" : "ok",
      "time" : f"{start_at} - {end_at} - duration: {duration:.1f} seconds",
      "msg" : f"From Pod: {os.getenv('HOSTNAME')}"
      }, 200

@app.route('/health')
def health():
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)