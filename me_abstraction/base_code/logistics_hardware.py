from config.config_manager import ConfigManager

# Some of the configurations that logistics team wants to store.
def store_mysql_config(mysql_config):
    print('Storing mysql config of logistics team')
    ConfigManager.write_config('logistics_mysql_config.json', mysql_config)


def store_logistics_rest_server_config(rest_server_config):
    print('Storing rest_server config of logistics team')
    ConfigManager.write_config('logistics_rest_server.json', rest_server_config)


def read_mysql_config():
    print('Reading mysql config of logistics team')
    mysql_config = ConfigManager.read_config('logistics_mysql_config.json')
    return mysql_config


def read_logistics_rest_server_config():
    print('Reading rest_server config of logistics team')
    rest_server_config = ConfigManager.read_config('logistics_rest_server.json')
    return rest_server_config
