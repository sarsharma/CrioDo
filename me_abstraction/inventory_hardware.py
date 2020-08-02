from config.config_manager_json import ConfigManagerJson

# Some of the configurations that inventory team wants to store.

# Choose the config manager - single line change and it will automatically use the right
# file type.
# You don't have to touch any of the functions in the file!
config_manager = ConfigManagerJson()

def store_mysql_config(mysql_config):
    print('Storing mysql config of inventory team')
    config_manager.write_config('inventory_mysql_config', mysql_config)


def read_mysql_config():
    print('Reading mysql config of inventory team')
    mysql_config = config_manager.read_config('inventory_mysql_config')
    return mysql_config

