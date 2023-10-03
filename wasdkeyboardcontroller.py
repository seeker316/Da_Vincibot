import msvcrt

angles = [0, 0, 0, 0, 0]
upper_limits = [180, 90, 90, 180, 90]
lower_limits = [0, 0, 0, 0, 0]

#### wasd for the full control of the bot 
# a, d for controlling the bse
# r, f for controliing the shoulder joint 
# t, g for controlling the elbow joint 


while True:
    # Check if a key is pressed
    if msvcrt.kbhit():
        key = msvcrt.getch()
        print(f"Pressed key: {key}")  # Debugging line
        
        # Handle letter keys
        key = key.decode('utf-8')
        
        if key == 'w':  # Up arrow key
                if angles[1] < upper_limits[1]: 
                    angles[1] += 1
                elif angles[2] < upper_limits[2]:
                    angles[2] += 1
                elif angles[4] < upper_limits[4]:
                    angles[4] +=1
                else:
                    print("Da_vinvibot has reached its upper limit")
        elif key == 's':  # Down arrow key
                if angles[4] > lower_limits[4]: 
                    angles[4] -= 1
                elif angles[2] > lower_limits[2]:
                    angles[2] -= 1
                elif angles[1] > lower_limits[1]:
                    angles[1] -= 1
                else:
                    print("Da_vinvibot has reached its lower limit")
        elif key == 'd':  # moving base right
            if angles[0] < upper_limits[0]:
                angles[0] += 1
            else:
                print("Da_vincibot base has reached its upper limit")
        elif key == 'a':  # moving base left
            if angles[0] > lower_limits[0]:
                angles[0] -= 1
            else:
                print("Da_vincibot base has reached its lower limit")
        elif key == 'r':  # moving shoulder up
            if angles[1] < upper_limits[1]:
                angles[1] += 1
            else:
                print("Da_vincibot shoulder has reached its upper limit")
        elif key == 'f':  # moving shoulder down
            if angles[1] > lower_limits[1]:
                angles[1] -= 1
            else:
                print("Da_vincibot shoulder has reached its lower limit")
        elif key == 't':  # moving elbow up
            if angles[2] < upper_limits[2]:
                angles[2] += 1
            else:
                print("Da_vincibot elbow has reached its upper limit")
        elif key == 'g':  # moving elbow down
            if angles[2] > lower_limits[2]:
                angles[2] -= 1
            else:
                print("Da_vincibot elbow has reached its lower limit")
        elif key == 'y':  # rotating wrist
            if angles[3] < upper_limits[3]:
                angles[3] += 1
            else:
                print("Da_vincibot wrist has reached its right limit")
        elif key == 'h':  # rotating wrist --
            if angles[3] > lower_limits[3]:
                angles[3] -= 1
            else:
                print("Da_vincibot wrist has reached its left limit")
        elif key == 'u':  # moving wrist up
            if angles[4] < upper_limits[4]:
                angles[4] += 1
            else:
                print("Da_vincibot wrist has reached its upper limit")
        elif key == 'j':  # moving wrist down
            if angles[4] > lower_limits[4]:
                angles[4] -= 1
            else:
                print("Da_vincibot wrist has reached its lower limit")
        else:
            print("ERROR invalid input")

    # Print the updated angles
    print(f"Da_vincibot angles: {angles}", end='\r')
