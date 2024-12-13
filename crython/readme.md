```
import crython
import os

# Read the cron expression from an environment variable, with a default value
CRON_EXPRESSION = os.getenv("CRON_EXPRESSION", "*/5 * * * *")  # Default: Every 5 minutes

# Define the Crython job using the cron expression
@crython.job(CRON_EXPRESSION)
def my_scheduled_task():
    print("Hello from Crython! Your task is running.")

if __name__ == "__main__":
    print(f"Starting Crython scheduler with CRON_EXPRESSION: {CRON_EXPRESSION}")
    crython.start()

    # Keep the main thread alive to allow jobs to run
    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        print("Stopping Crython scheduler...")
        crython.stop()
```
