from config.config_manager import ConfigManager

# Some of the configurations that vendor management team wants to store.

def store_mysql_config(mysql_config):
    print('Storing mysql config of vendor management team')
    ConfigManager.write_config('vendor_mysql_config.json', mysql_config)


def store_resolv_config(resolv_config):
    print('Storing resolv config of all vendor management servers')
    ConfigManager.write_config('vendor_server_resolv_config.json', resolv_config)


def read_mysql_config():
    print('Reading mysql config of vendor management team')
    mysql_config = ConfigManager.read_config('vendor_mysql_config.json')
    return mysql_config


def read_resolv_config():
    print('Reading resolv config vendor management servers')
    resolv_config = ConfigManager.read_config('vendor_server_resolv_config.json')
    return resolv_config
