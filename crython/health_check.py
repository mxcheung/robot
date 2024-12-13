```
import sys

def check_health():
    # Add your health check logic here
    # For example, check if a specific file exists or if a service is running
    try:
        # Check if a specific condition is met (e.g., service is running)
        # Example: Check if a process is running
        import os
        if os.system('pgrep my-app > /dev/null') == 0:
            print("Application is healthy.")
            return 0  # healthy
        else:
            print("Application is not healthy.")
            return 1  # unhealthy
    except Exception as e:
        print(f"Health check failed: {e}")
        return 1  # unhealthy

if __name__ == "__main__":
    sys.exit(check_health())
```
