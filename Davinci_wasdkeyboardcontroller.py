import keyboard
import time
import sys

angles = [0, 0, 0, 0, 0]
upper_limits = [180, 90, 90, 180, 90]
lower_limits = [0, 0, 0, 0, 0]
angle_increment = 1  # Adjust this value to control the speed of movement

def clear_line():
    sys.stdout.write("\033[K")  # Clear the current line in the terminal

while True:
    clear_line()  # Clear the previous line
    # Check if any key is pressed
    if keyboard.is_pressed('w') or keyboard.is_pressed('s') or keyboard.is_pressed('d') or keyboard.is_pressed('a') or keyboard.is_pressed('r') or keyboard.is_pressed('f') or keyboard.is_pressed('t') or keyboard.is_pressed('g') or keyboard.is_pressed('y') or keyboard.is_pressed('h') or keyboard.is_pressed('u') or keyboard.is_pressed('j'):
        # Update angles based on keypresses
        if keyboard.is_pressed('w'):  # Up arrow key
            if angles[1] < upper_limits[1]: 
                angles[1] += angle_increment
            elif angles[2] < upper_limits[2]:
                angles[2] += angle_increment
            elif angles[4] < upper_limits[4]:
                angles[4] += angle_increment
            else:
                print("Da_vincibot has reached its upper limit")
            time.sleep(0.1)  # Add a delay to control the speed of movement
        elif keyboard.is_pressed('s'):  # Down arrow key
            if angles[4] > lower_limits[4]: 
                angles[4] -= angle_increment
            elif angles[2] > lower_limits[2]:
                angles[2] -= angle_increment
            elif angles[1] > lower_limits[1]:
                angles[1] -= angle_increment
            else:
                print("Da_vincibot has reached its lower limit")
            time.sleep(0.1)  # Add a delay to control the speed of movement
        elif keyboard.is_pressed('d'):  # moving base right
            if angles[0] < upper_limits[0]:
                angles[0] += angle_increment
            else:
                print("Da_vincibot base has reached its upper limit")
            time.sleep(0.1)  # Add a delay to control the speed of movement
        elif keyboard.is_pressed('a'):  # moving base left
            if angles[0] > lower_limits[0]:
                angles[0] -= angle_increment
            else:
                print("Da_vincibot base has reached its lower limit")
            time.sleep(0.1)  # Add a delay to control the speed of movement
        elif keyboard.is_pressed('r'):  # moving shoulder up
            if angles[1] < upper_limits[1]:
                angles[1] += angle_increment
            else:
                print("Da_vincibot shoulder has reached its upper limit")
            time.sleep(0.1)  # Add a delay to control the speed of movement
        elif keyboard.is_pressed('f'):  # moving shoulder down
            if angles[1] > lower_limits[1]:
                angles[1] -= angle_increment
            else:
                print("Da_vincibot shoulder has reached its lower limit")
            time.sleep(0.1)  # Add a delay to control the speed of movement
        elif keyboard.is_pressed('t'):  # moving elbow up
            if angles[2] < upper_limits[2]:
                angles[2] += angle_increment
            else:
                print("Da_vincibot elbow has reached its upper limit")
            time.sleep(0.1)  # Add a delay to control the speed of movement
        elif keyboard.is_pressed('g'):  # moving elbow down
            if angles[2] > lower_limits[2]:
                angles[2] -= angle_increment
            else:
                print("Da_vincibot elbow has reached its lower limit")
            time.sleep(0.1)  # Add a delay to control the speed of movement
        elif keyboard.is_pressed('y'):  # rotating wrist
            if angles[3] < upper_limits[3]:
                angles[3] += angle_increment
            else:
                print("Da_vincibot wrist has reached its right limit")
            time.sleep(0.1)  # Add a delay to control the speed of movement
        elif keyboard.is_pressed('h'):  # rotating wrist --
            if angles[3] > lower_limits[3]:
                angles[3] -= angle_increment
            else:
                print("Da_vincibot wrist has reached its left limit")
            time.sleep(0.1)  # Add a delay to control the speed of movement
        elif keyboard.is_pressed('u'):  # moving wrist up
            if angles[4] < upper_limits[4]:
                angles[4] += angle_increment
            else:
                print("Da_vincibot wrist has reached its upper limit")
            time.sleep(0.1)  # Add a delay to control the speed of movement
        elif keyboard.is_pressed('j'):  # moving wrist down
            if angles[4] > lower_limits[4]:
                angles[4] -= angle_increment
            else:
                print("Da_vincibot wrist has reached its lower limit")
            time.sleep(0.1)  # Add a delay to control the speed of movement
    else:
        pass  # Do nothing if no control key is pressed

    # Print the updated angles
    sys.stdout.write(f"Da_vincibot angles: {angles}\r")
    sys.stdout.flush()  # Flush the output to ensure it's displayed immediately

