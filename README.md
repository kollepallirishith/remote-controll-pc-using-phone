# Remote Touchpad Controller

## Overview
The **Remote Touchpad Controller** is a Python Flask application that allows users to control their PC's mouse and keyboard using a touch screen device. This project leverages the Flask framework for creating a web interface and `pyautogui` for mouse and keyboard control.

## Features
- **Touch Input**: Move the mouse cursor by swiping on the touch screen.
- **Mouse Clicks**: Perform left and right clicks using buttons.
- **Keyboard Input**: Type text into the PC's keyboard.
- **Backspace and Enter**: Send backspace and enter key commands.

## Requirements
- Python 3.x
- Flask
- pyautogui

## Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/remote_touchpad_controller.git
cd remote_touchpad_controller
#!/bin/bash

# Remote Touchpad Controller Setup Script

echo "=== Remote Touchpad Controller Setup ==="

# Step 1: Clone the repository
echo "Step 1: Cloning the repository..."
git clone https://github.com/yourusername/remote_touchpad_controller.git
cd remote_touchpad_controller || { echo "Failed to change directory."; exit 1; }

# Step 2: Install dependencies
echo "Step 2: Installing necessary dependencies..."
python3 -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate the virtual environment
pip install Flask pyautogui  # Install required packages

# Step 3: Run the application
echo "Step 3: Starting the Flask application..."
python app.py &  # Run the application in the background

# Instructions
echo ""
echo "=== Instructions ==="
echo "1. Open a web browser on your touch screen device."
echo "2. Navigate to http://<your_ip>:8080."
echo "3. Use the touch area to move the mouse cursor."
echo "4. Click the buttons for left and right clicks, type text, and use backspace and enter functions as needed."
echo ""
echo "=== Troubleshooting ==="
echo "1. Ensure that your firewall allows traffic on port 8080."
echo "2. If you encounter permission issues with pyautogui, try running the script with administrative privileges."
echo "3. Check the console output for any error messages if something isn't working as expected."
echo ""
echo "=== License ==="
echo "This project is licensed under the MIT License. See the LICENSE file for details."
echo ""
echo "=== Acknowledgments ==="
echo "Flask Documentation: https://flask.palletsprojects.com/"
echo "pyautogui Documentation: https://pyautogui.readthedocs.io/en/latest/"
echo ""
echo "=== Contact ==="
echo "For any questions or suggestions, feel free to reach out:"
echo "Email: your_email@example.com"
echo "GitHub: https://github.com/yourusername"

echo "Setup complete! Enjoy using the Remote Touchpad Controller."
