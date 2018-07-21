

class GameRunTimeException(RuntimeError):
    pass


class ParseAssetException(StandardError):
    pass


class GameInvalidChoice(GameRunTimeException):
    pass


class GameOverException(GameRunTimeException):
    pass


class GameNotOperating(GameRunTimeException):
    pass


class GameLoadClassException(GameRunTimeException):
    pass


class NoSuchParser(ParseAssetException):
    pass


class NoTypeSpecified(ParseAssetException):
    pass


class GameNavigateFailure(GameRunTimeException):
    pass


class GameLibraryDoesNotExist(GameLoadClassException):
    pass


class GameClassDoesNotExist(GameLoadClassException):
    pass


class GameConfigurationException(Exception):
    pass
