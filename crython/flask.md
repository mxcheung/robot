```
import os
import crython
from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# Read the cron expression from an environment variable, with a default value
CRON_EXPRESSION = os.getenv("CRON_EXPRESSION", "*/5 * * * *")  # Default: Every 5 minutes

# Define the Crython job using the cron expression
@crython.job(CRON_EXPRESSION)
def my_scheduled_task():
    print("Hello from Crython! Your task is running.")

# Health check endpoint
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "Application is running"}), 200

if __name__ == "__main__":
    print(f"Starting Crython scheduler with CRON_EXPRESSION: {CRON_EXPRESSION}")
    crython.start()

    # Start Flask app on a separate thread
    try:
        app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
    except (KeyboardInterrupt, SystemExit):
        print("Stopping Crython scheduler...")
        crython.stop()
```
