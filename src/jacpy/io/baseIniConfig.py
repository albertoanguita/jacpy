import configparser

from ..object.Singleton import Singleton


# todo turn into singleton
class BaseIniConfig(Singleton):

    def __init__(self, path: str):
        if not self._initialized:
            self.__config = configparser.ConfigParser()
            self.__config.read(path)
            self._initialized = True

    def _get_str_value(self, section: str, key) -> str:
        return self.__config[section][key]

    def _get_int_value(self, section: str, key) -> int:
        return int(self.__config[section][key])

    def items(self):
        return self.__config.items()
