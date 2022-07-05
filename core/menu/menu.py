from pathlib import Path

#
#   Show exercises list
#
def print_options(options):
    print("\n\n")
    print("============")
    print("    MENU    ")
    print("============")
    print("\n")
    print("Exercises: ", [elem for elem in options])
    print("Exit: (0)")


#
#   Input option data
#
def select_option():
    return int(input("\nIngrese el número del ejercicio: "))


#
#   Call the exercise file
#
def launch_exercise(option):
    abs_path = Path(__file__)
    parent_dir = abs_path.parent.parent.absolute()
    exercise_file = str(parent_dir) + "/exercises/ejercicio_" + str(option) + ".py"
    exec(open(exercise_file).read())
