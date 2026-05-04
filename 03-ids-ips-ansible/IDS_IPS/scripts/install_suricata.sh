#!/bin/bash

echo "Updating system..."
sudo apt update && sudo apt upgrade -y

echo "Installing Suricata..."
sudo apt install suricata -y

echo "Updating Suricata rules..."
sudo suricata-update

echo "Enabling Suricata service..."
sudo systemctl enable suricata
sudo systemctl start suricata

echo "Suricata installation completed."