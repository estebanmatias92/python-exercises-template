from .menu.menu import *
import os

# List of options
OPTIONS = range(1, 11)

#
#   Main loop for menu
#
def init_app(options):
    # Emulate a do-while loop, this always is going to execute at least one time
    while True:
        # Show all the exercise options
        print_options(options)

        # Get the input from the user
        option = select_option()

        # If the option is Exit or is not in the list of exercises, get out
        if (option == 0) or not (option in options):
            break

        # Clear the terminal after each exercise
        os.system("clear")

        # Launch the exercise function
        launch_exercise(option)

    # Clear terminal after ending the program
    os.system("clear")
