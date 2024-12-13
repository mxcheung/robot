```
import os
import crython
import threading
from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# Read the cron expression from an environment variable, with a default value
CRON_EXPRESSION = os.getenv("CRON_EXPRESSION", "*/5 * * * *")  # Default: Every 5 minutes

# Global flag for batch job
batch_job_flag = {"run_batch": False}

# Batch job function
def run_batch_job():
    print("Running batch job...")
    # Simulate batch job execution
    print("Batch job completed.")

# Crython job to check the batch job flag
@crython.job("*/1 * * * *")  # Check every minute
def check_and_run_batch_job():
    if batch_job_flag["run_batch"]:
        print("Flag detected. Starting batch job...")
        run_batch_job()
        batch_job_flag["run_batch"] = False  # Reset the flag
    else:
        print("No batch job triggered.")

# Health check endpoint
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "Application is running"}), 200

# Endpoint to trigger the batch job
@app.route("/trigger-batch", methods=["POST"])
def trigger_batch():
    batch_job_flag["run_batch"] = True
    return jsonify({"status": "ok", "message": "Batch job triggered"}), 200

if __name__ == "__main__":
    # Start Crython scheduler
    print(f"Starting Crython scheduler with CRON_EXPRESSION: {CRON_EXPRESSION}")
    crython.start()

    # Start Flask app in a separate thread
    flask_thread = threading.Thread(target=lambda: app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False))
    flask_thread.start()

    # Keep the main thread alive to allow Crython jobs to run
    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        print("Stopping Crython scheduler...")
        crython.stop()
```
