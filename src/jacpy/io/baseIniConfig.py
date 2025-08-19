import configparser

from ..object.Singleton import Singleton


# todo turn into singleton
class BaseIniConfig(Singleton):

    def __init__(self, path: str):
        if not self._initialized:
            self.__config = configparser.ConfigParser()
            self.__config.read(path)
            self._initialized = True

    def _get_str_value(self, section: str, key: str) -> str:
        return self.__config[section][key]

    def _get_int_value(self, section: str, key: str) -> int:
        return int(self.__config[section][key])

    def _get_float_value(self, section: str, key: str) -> float:
        return float(self.__config[section][key])

    def _get_bool_value(self, section: str, key: str) -> bool:
        return self.__config[section][key].lower() == 'true'

    def _set_value(self, section: str, key: str, value) -> None:
        self.__config[section][key] = value

    def items(self):
        return self.__config.items()
