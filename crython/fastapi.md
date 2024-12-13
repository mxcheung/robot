```
fastapi
uvicorn
crython
```

```
import os
import crython
import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Read the cron expression from an environment variable, with a default value
CRON_EXPRESSION = os.getenv("CRON_EXPRESSION", "*/5 * * * *")  # Default: Every 5 minutes

# Global flag for batch job
batch_job_flag = {"run_batch": False}

# Batch job function
async def run_batch_job():
    print("Running batch job...")
    # Simulate batch job execution with async sleep
    await asyncio.sleep(2)
    print("Batch job completed.")

# Crython job to check the batch job flag
@crython.job("*/1 * * * *")  # Check every minute
def check_and_run_batch_job():
    if batch_job_flag["run_batch"]:
        print("Flag detected. Starting batch job...")
        asyncio.run(run_batch_job())
        batch_job_flag["run_batch"] = False  # Reset the flag
    else:
        print("No batch job triggered.")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Application is running"}

# Request model for batch trigger endpoint
class TriggerBatchRequest(BaseModel):
    trigger: bool

# Endpoint to trigger the batch job
@app.post("/trigger-batch")
async def trigger_batch(request: TriggerBatchRequest):
    if request.trigger:
        batch_job_flag["run_batch"] = True
        return {"status": "ok", "message": "Batch job triggered"}
    return {"status": "ok", "message": "Batch job not triggered"}

# Start Crython scheduler on application startup
@app.on_event("startup")
async def startup_event():
    print(f"Starting Crython scheduler with CRON_EXPRESSION: {CRON_EXPRESSION}")
    crython.start()

# Stop Crython scheduler on application shutdown
@app.on_event("shutdown")
async def shutdown_event():
    print("Stopping Crython scheduler...")
    crython.stop()
```

