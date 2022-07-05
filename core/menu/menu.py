import os

# from os import listdir
# from os.path import isfile, join
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

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
#   Call the exercise module
#
def launch_exercise(option):
    name = "ejercicio_" + str(option)
    # exercise = getattr(exercises, "ejercicio_%i.py" % option)
    # exercise.launch()
    # ejercicio_1.launch()
    module_list = [
        str(elem).replace(".py", "") for elem in os.listdir("./core/exercises")
    ]
    # module_list[].launch()

    # print(dir(exercises.__name__))
    exec(module_list[0]).launch()
