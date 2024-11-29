import psutil
import time

def monitor_cpu(threshold):
    """
    Function to monitor CPU usage and alert when it exceeds a specified threshold.
    :param threshold: The CPU usage percentage threshold to trigger an alert.
    """
    print("Monitoring CPU usage...")  # Inform the user that monitoring has started
    try:
        while True:
            # Get the current CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # Check if the CPU usage exceeds the threshold
            if cpu_usage > threshold:
                print(f"⚠️ Alert! CPU usage exceeds threshold: {cpu_usage}%")
            else:
                print(f"CPU Usage: {cpu_usage}%")  # Display current CPU usage
    except KeyboardInterrupt:
        # Gracefully handle script interruption
        print("\nMonitoring stopped.")
    except Exception as e:
        # Handle any unexpected errors
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # Set the CPU usage threshold
    threshold = 80  # Adjust this value as needed
    
    # Start monitoring the CPU
    monitor_cpu(threshold)
