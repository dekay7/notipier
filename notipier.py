import requests
import socket
import subprocess
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve webhook URL from environment variable
webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

def get_internal_ip():
    """Gets the internal IP address of the computer."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1", 80))
    internal_ip = s.getsockname()[0]
    s.close()
    return internal_ip

def get_external_ip():
    """Gets the external IP address of the computer."""
    response = requests.get("https://ifconfig.me/ip")
    return response.text.strip()

def get_system_info():
    """Gathers important system information."""
    os_name = subprocess.check_output(["uname", "-o"]).decode().strip()
    hostname = subprocess.check_output(["hostname"]).decode().strip()
    uptime = subprocess.check_output(["uptime", "-p"]).decode().strip()
    return f"OS: {os_name}\nHostname: {hostname}\nUptime: {uptime}"

def send_discord_message(message):
    """Sends a message to Discord using the webhook."""
    data = {"content": message}
    requests.post(webhook_url, json=data)

if __name__ == "__main__":
    internal_ip = get_internal_ip()
    external_ip = get_external_ip()
    system_info = get_system_info()

    message = f"**System Booted**\n\nInternal IP: {internal_ip}\nExternal IP: {external_ip}\n\n{system_info}"

    send_discord_message(message)