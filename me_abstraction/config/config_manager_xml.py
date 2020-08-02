import dict2xml as dict2xml
import xmltodict as xmltodict

from config.config_manager import ConfigManager

# XML implementation of config manager.
class ConfigManagerXml(ConfigManager):
    CONFIG_FOLDER = 'oop_way/config_files/'
    FILE_SUFFIX = '.xml'

    def read_config(self, filename: str):
        with open(ConfigManager.CONFIG_FOLDER + filename
                  + ConfigManagerXml.FILE_SUFFIX) as fd:
            config_data = xmltodict.parse(fd.read())
        return dict(config_data['config'])


    def write_config(self, filename: str, config_data: dict):
        xml = dict2xml.dict2xml(config_data, wrap ='config')
        xmlfile = open(ConfigManager.CONFIG_FOLDER + filename
                       + ConfigManagerXml.FILE_SUFFIX, "w")
        xmlfile.write(xml)
        xmlfile.close()

