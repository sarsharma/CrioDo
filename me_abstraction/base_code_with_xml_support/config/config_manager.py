import json
import os

import dict2xml as dict2xml
import xmltodict as xmltodict

# Config Manager to help teams store and read back configuration from persistent storage.
class ConfigManager:
    CONFIG_FOLDER = 'base_code_with_xml_support/config_files/'

    @staticmethod
    def read_config_from_json(filename):
        with open(ConfigManager.CONFIG_FOLDER + filename) as inputfile:
            try:
                config_data = json.load(inputfile)
                return config_data
            except:
                print('Seems the file is empty. Not a problem')


    @staticmethod
    def write_config_to_json(filename, config_data):
        with open(ConfigManager.CONFIG_FOLDER + filename, 'w') as outfile:
            json.dump(config_data, outfile)
            outfile.write('\n')


    @staticmethod
    def read_config_from_xml(filename):
        with open(ConfigManager.CONFIG_FOLDER + filename) as fd:
            config_data = xmltodict.parse(fd.read())
        return dict(config_data['config'])


    @staticmethod
    def write_config_to_xml(filename, config_data):
        xml = dict2xml.dict2xml(config_data, wrap ='config')
        xmlfile = open(ConfigManager.CONFIG_FOLDER + filename, "w")
        xmlfile.write(xml)
        xmlfile.close()

    @staticmethod
    def read_config_from_csv(filename):
        # Similarly you can write this function to read from csv
        pass


    @staticmethod
    def write_config_to_csv(filename, config_data):
        # Similarly you can write this function to write to csv
        pass


# Static initialization of config directory.
# Ignore code.
try:
    os.stat(ConfigManager.CONFIG_FOLDER)
except:
    os.mkdir(ConfigManager.CONFIG_FOLDER)
