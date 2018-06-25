

class GameRunTimeException(RuntimeError):
    pass


class GameLoadClassException(GameRunTimeException):
    pass


class GameLibraryDoesNotExist(GameLoadClassException):
    pass


class GameClassDoesNotExist(GameLoadClassException):
    pass


class GameConfigurationException(Exception):
    pass
