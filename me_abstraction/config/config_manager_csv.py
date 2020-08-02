from config.config_manager import ConfigManager

# CSV implementation of config manager.
class ConfigManagerCsv(ConfigManager):
    CONFIG_FOLDER = 'oop_way/config_files/'
    FILE_SUFFIX = '.csv'

    def read_config(self, filename: str):
        # Similarly you can write this function to read from csv
        pass


    def write_config(self, filename: str, config_data: dict):
        # Similarly you can write this function to write to csv
        pass

