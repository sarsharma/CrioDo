import abc
import os

# Abstract Config Manager to help teams store and read back configuration from persistent storage.
# This class doesn't not have any implementation.
# The class exposes two functions
# - read_config
# - write_config
#
# Developers in Configuration Management team can choose to have
# multiple implementations for the functions based on the type of config file:
#   - Implement functions to store/retrieve data from csv file
#   - Implement functions to store/retrieve data from json file
#   - Implement functions to store/retrieve data from xml file

class ConfigManager(metaclass=abc.ABCMeta):
    CONFIG_FOLDER = 'oop_way/config_files/'

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'read_config') and
                callable(subclass.read_config) and
                hasattr(subclass, 'write_config') and
                callable(subclass.write_config) or
                NotImplemented)

    @abc.abstractmethod
    def read_config(self, filename: str):
        print('Abstract method: Not implemented')
        raise NotImplementedError

    @abc.abstractmethod
    def write_config(self, filename: str, config_data: dict):
        print('Abstract method: Not implemented')
        raise NotImplementedError

# Static initialization of config directory.
# Ignore code.
try:
    os.stat(ConfigManager.CONFIG_FOLDER)
except:
    os.mkdir(ConfigManager.CONFIG_FOLDER)
