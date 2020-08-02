import json
import os

# Config Manager to help teams store and read back configuration from persistent storage.
class ConfigManager:
    CONFIG_FOLDER = 'base_code/config_files/'

    @staticmethod
    def read_config(filename):
        with open(ConfigManager.CONFIG_FOLDER + filename) as inputfile:
            try:
                config_data = json.load(inputfile)
                return config_data
            except:
                print('Seems the file is empty. Not a problem')


    @staticmethod
    def write_config(filename, config_data):
        with open(ConfigManager.CONFIG_FOLDER + filename, 'w') as outfile:
            json.dump(config_data, outfile)
            outfile.write('\n')


# Static initialization of config directory.
# Ignore code.
try:
    os.stat(ConfigManager.CONFIG_FOLDER)
except:
    os.mkdir(ConfigManager.CONFIG_FOLDER)
