import os
import time
from subprocess import run

def run_robot_script():
    print(f"Running Robot Framework script at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    result = run(["robot", "hello.robot"])  # Replace 'test.robot' with your script file
    if result.returncode == 0:
        print("Script executed successfully.")
    else:
        print(f"Script failed with return code {result.returncode}")

if __name__ == "__main__":
    print("Starting Robot Framework execution loop...")
    while True:
        run_robot_script()
        print("Sleeping for 1 hour...")
        time.sleep(60)  # Sleep for 1 minute
