#!/bin/bash

echo "Starting Robot Framework execution loop..."

while true; do
    echo "Running Robot Framework script at $(date)"
    robot hello.robot  # Replace with the path to your Robot Framework script
    echo "Sleeping for 1 hour..."
    sleep 3600  # Sleep for 3600 seconds (1 hour)
done
