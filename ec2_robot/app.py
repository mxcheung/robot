import os
import time
from subprocess import run

def run_robot_script():
    output_dir = "/tests/output"
    os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists
    print(f"Running Robot Framework script at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    result = run([
        "robot",
        "--pythonpath", "/tests",  # Ensure the test.py module is accessible
        "--outputdir", output_dir,  # Specify the output directory
        "hello.robot"
    ])
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
