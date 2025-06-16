import requests
import time
import os

# --- Configuration ---

# Replace this with the actual URL of your Render service
# Example: "https://your-service-name.onrender.com"
# Make sure to include http:// or https://
RENDER_SERVICE_URL = "YOUR_RENDER_SERVICE_URL_HERE"

# How often to send a request, in seconds.
# Render's free tier idles after 15 minutes (900 seconds) of inactivity.
# Set this value to something slightly less than 900 seconds (e.g., 14 minutes = 840 seconds)
REQUEST_INTERVAL_SECONDS = 840

# --- Script Logic ---

def send_request(url):
    """Sends a GET request to the specified URL and prints the status."""
    try:
        print(f"[{time.ctime()}] Sending GET request to {url}...")
        response = requests.get(url, timeout=10) # Set a timeout to prevent hanging
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

        print(f"[{time.ctime()}] Request successful. Status code: {response.status_code}")

    except requests.exceptions.Timeout:
        print(f"[{time.ctime()}] Request timed out after 10 seconds.")
    except requests.exceptions.RequestException as e:
        print(f"[{time.ctime()}] Error sending request: {e}")
    except Exception as e:
        print(f"[{time.ctime()}] An unexpected error occurred: {e}")

if __name__ == "__main__":
    if RENDER_SERVICE_URL == "YOUR_RENDER_SERVICE_URL_HERE" or not RENDER_SERVICE_URL:
        print("Error: Please replace 'YOUR_RENDER_SERVICE_URL_HERE' with your actual Render service URL.")
        exit()

    print(f"Starting Render service keep-alive script.")
    print(f"Target URL: {RENDER_SERVICE_URL}")
    print(f"Interval: {REQUEST_INTERVAL_SECONDS} seconds ({REQUEST_INTERVAL_SECONDS / 60:.1f} minutes)")
    print("Press Ctrl+C to stop.")

    while True:
        send_request(RENDER_SERVICE_URL)

        # Wait for the specified interval before the next request
        print(f"[{time.ctime()}] Waiting for {REQUEST_INTERVAL_SECONDS} seconds...")
        time.sleep(REQUEST_INTERVAL_SECONDS)
