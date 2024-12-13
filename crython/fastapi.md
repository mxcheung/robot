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
from contextlib import asynccontextmanager

# Read the cron expression from an environment variable, with a default value
CRON_EXPRESSION = os.getenv("CRON_EXPRESSION", "*/5 * * * *")  # Default: Every 5 minutes

# Global flag for batch job
batch_job_flag = {"run_batch": False}

# Batch job function
async def run_batch_job():
    print("Running batch job...")
    await asyncio.sleep(2)  # Simulate batch job execution
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

# Define lifespan for startup and shutdown events
@asynccontextmanager
async def app_lifespan(app: FastAPI):
    print(f"Starting Crython scheduler with CRON_EXPRESSION: {CRON_EXPRESSION}")
    crython.start()
    try:
        yield  # Application is running
    finally:
        print("Stopping Crython scheduler...")
        crython.stop()

# Initialize FastAPI app with lifespan
app = FastAPI(lifespan=app_lifespan)

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
```

```
DeprecationWarning: 
        on_event is deprecated, use lifespan event handlers instead.
        Read more about it in the
        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
```
