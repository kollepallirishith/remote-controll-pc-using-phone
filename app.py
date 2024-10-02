from flask import Flask, render_template, request, jsonify
import pyautogui
import time

app = Flask(__name__)

# Store the last known cursor position for tracking
current_x, current_y = pyautogui.position()
target_x, target_y = current_x, current_y  # Track target positions
smoothing_factor = 0.5  # Lower value for smoother movement

# Define your phone's screen resolution (in pixels)
PHONE_SCREEN_WIDTH = 1080  # Replace with your phone's actual screen width
PHONE_SCREEN_HEIGHT = 2400  # Replace with your phone's actual screen height

# Get the PC screen resolution
PC_SCREEN_WIDTH, PC_SCREEN_HEIGHT = pyautogui.size()
print(f"PC Screen Resolution: {PC_SCREEN_WIDTH} x {PC_SCREEN_HEIGHT}")

# Throttle updates
last_update_time = time.time()
update_interval = 0.01  # Update every 10 milliseconds

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Receive touch data from the phone and move the mouse pointer
@app.route('/touch_data', methods=['POST'])
def touch_data():
    global current_x, current_y, last_update_time
    try:
        data = request.get_json()  # Ensure JSON is properly parsed
        if 'delta_x' not in data or 'delta_y' not in data:
            return jsonify({"status": "error", "message": "Invalid data"}), 400
        
        # Get current delta values from the phone's trackpad
        delta_x, delta_y = data['delta_x'], data['delta_y']
        print(f"Delta values received: delta_x: {delta_x}, delta_y: {delta_y}")

        # Apply scaling if needed
        scale_factor = 1.0  # Lower scale factor for smoother movement
        delta_x_scaled = delta_x * scale_factor
        delta_y_scaled = delta_y * scale_factor

        # Implement dead zone
        DEAD_ZONE = 2
        if abs(delta_x_scaled) < DEAD_ZONE and abs(delta_y_scaled) < DEAD_ZONE:
            return jsonify({"status": "success", "message": "No significant movement"}), 200

        # Check update frequency
        if time.time() - last_update_time < update_interval:
            return jsonify({"status": "error", "message": "Too frequent updates"}), 429

        # Update last update time
        last_update_time = time.time()

        # Calculate new target position
        target_x = current_x + delta_x_scaled
        target_y = current_y + delta_y_scaled

        # Constrain the target position to the screen bounds
        target_x = max(0, min(target_x, PC_SCREEN_WIDTH - 1))
        target_y = max(0, min(target_y, PC_SCREEN_HEIGHT - 1))

        # Smooth movement: interpolate towards the target position
        current_x += (target_x - current_x) * smoothing_factor
        current_y += (target_y - current_y) * smoothing_factor

        # Move the mouse pointer to the updated position
        pyautogui.moveTo(int(current_x), int(current_y))

        print(f"Moving mouse to: ({int(current_x)}, {int(current_y)})")
        return jsonify({"status": "success", "message": "Touch data received"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": "Server error"}), 500

# Left click route
@app.route('/left_click', methods=['POST'])
def left_click():
    try:
        pyautogui.click(button='left')
        print("Left click executed")
        return jsonify({"status": "success", "message": "Left click executed"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": "Server error"}), 500

# Right click route
@app.route('/right_click', methods=['POST'])
def right_click():
    try:
        pyautogui.click(button='right')
        print("Right click executed")
        return jsonify({"status": "success", "message": "Right click executed"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": "Server error"}), 500

# Keyboard input route
@app.route('/keyboard_input', methods=['POST'])
def keyboard_input():
    try:
        data = request.get_json()
        if 'text' not in data:
            return jsonify({"status": "error", "message": "Invalid data"}), 400

        text = data['text']
        print(f"Keyboard input received: {text}")

        # Type the text using pyautogui
        pyautogui.typewrite(text)
        return jsonify({"status": "success", "message": "Text typed"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": "Server error"}), 500

# Backspace route
@app.route('/backspace', methods=['POST'])
def backspace():
    try:
        pyautogui.press('backspace')
        print("Backspace executed")
        return jsonify({"status": "success", "message": "Backspace executed"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": "Server error"}), 500

# Enter route
@app.route('/enter', methods=['POST'])
def enter():
    try:
        pyautogui.press('enter')
        print("Enter executed")
        return jsonify({"status": "success", "message": "Enter executed"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": "Server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
