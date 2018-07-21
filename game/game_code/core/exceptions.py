

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


class LoadModuleException(GameRunTimeException):
    pass


class NoSuchParser(ParseAssetException):
    pass


class NoTypeSpecified(ParseAssetException):
    pass


class AssetNotLoaded(ParseAssetException):
    pass


class GameNavigateFailure(GameRunTimeException):
    pass


class LoadLibraryDoesNotExist(LoadModuleException):
    pass


class LoadClassDoesNotExist(LoadModuleException):
    pass


class LoadVariableDoesNotExist(LoadModuleException):
    pass


class GameConfigurationException(Exception):
    pass
