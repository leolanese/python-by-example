import os
import platform

def clear_screen():
    # Detect the operating system
    operating_system = platform.system()

    # Use the appropriate command to clear the screen
    if operating_system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# Call the function to clear the screen
clear_screen()
