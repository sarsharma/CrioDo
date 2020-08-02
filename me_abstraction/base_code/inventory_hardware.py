from config.config_manager import ConfigManager

# Some of the configurations that inventory team wants to store.
def store_mysql_config(mysql_config):
    print('Storing mysql config of inventory team')
    ConfigManager.write_config('inventory_mysql_config.json', mysql_config)


def read_mysql_config():
    print('Reading mysql config of inventory team')
    mysql_config = ConfigManager.read_config('inventory_mysql_config.json')
    return mysql_config

