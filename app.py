import cv2
import numpy as np
import requests
import re

def scan_ip_camera(ip):
    url = f"http://{ip}/shot.jpg"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException as e:
        pass
    return False

def get_ip_cameras_in_network(network):
    ip_cameras = []
    for ip in range(1, 256):
        ip_address = f"{network}.{ip}"
        if scan_ip_camera(ip_address):
            ip_cameras.append(ip_address)
    return ip_cameras

def main():
    network = input("Enter the network address (e.g. 192.168.1): ")
    ip_cameras = get_ip_cameras_in_network(network)
    if ip_cameras:
        print("IP Cameras found:")
        for ip in ip_cameras:
            print(ip)
    else:
        print("ip camera not found")

if __name__ == "__main__":
    main()
