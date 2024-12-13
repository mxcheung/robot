#!/bin/bash

# Check if the Python scheduler process is running
if pgrep -f "scheduler.py" > /dev/null; then
    echo "Scheduler is healthy."
    exit 0
else
    echo "Scheduler is not healthy."
    exit 1
fi
