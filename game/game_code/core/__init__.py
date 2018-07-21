import os
import imp
import exceptions

this_file = os.path.realpath(__file__)
this_dir = os.path.dirname(this_file)
core_dir = this_dir
game_code_dir = os.path.dirname(core_dir)
game_dir = os.path.dirname(game_code_dir)
assets_dir = os.path.join(game_dir, 'assets')
levels_dir = os.path.join(game_code_dir, 'levels')


def load_class_from_file(file_path, class_name):
    """
    loads a class from a file using its string path relative to root
    :param file_path: the file_path to load
    :param class_name: the name of the class to load from the file
    :return:
    """
    module = load_module_from_path(file_path)
    # get class
    class_object = getattr(module, class_name)
    if class_object is None:
        raise exceptions.LoadClassDoesNotExist(class_name)
    # returns the class object (not initialized)
    return class_object


def load_variable_from_file(file_path, variable_name):
    """
    loads a variable from a file using its string path relative to root
    :param file_path: the file_path to load
    :param variable_name: the name of the class to load from the file
    :return:
    """
    module = load_module_from_path(file_path)
    # get class
    variable = getattr(module, variable_name)
    if variable is None:
        raise exceptions.LoadVariableDoesNotExist(variable_name)
    # returns the variable
    return variable


def load_module_from_path(file_path):
    # handle the file path to get the libray/module name (strip the extension off the basename)
    lib_name, extension = os.path.splitext(os.path.basename(file_path))
    # load module
    try:
        module = imp.load_source(lib_name, file_path)
    except IOError as exc:
        if exc.errno == 2:
            raise exceptions.LoadLibraryDoesNotExist(file_path)
        raise
    return module

