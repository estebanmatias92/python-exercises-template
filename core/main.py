from core.menu.menu import *
import os

# Path to exercises directory
EXERCISES_DIR = str(os.path.dirname(os.path.abspath(__file__))) + "/exercises"

#
#   Get all the exercises files as a list
#
def get_exercises_list():
    return os.listdir(EXERCISES_DIR)


# List of options
OPTIONS = range(1, len(get_exercises_list()) + 1)

#
#   Main loop for menu
#
def init_app(options):
    # Emulate a do-while loop, this always is going to execute at least one time
    while True:
        # Clear console
        os.system("clear")

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
