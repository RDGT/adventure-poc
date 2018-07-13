

class GameRunTimeException(RuntimeError):
    pass


class GameInvalidChoice(GameRunTimeException):
    pass


class GameLoadClassException(GameRunTimeException):
    pass


class GameNavigateFailure(GameRunTimeException):
    pass


class GameLibraryDoesNotExist(GameLoadClassException):
    pass


class GameClassDoesNotExist(GameLoadClassException):
    pass


class GameConfigurationException(Exception):
    pass
