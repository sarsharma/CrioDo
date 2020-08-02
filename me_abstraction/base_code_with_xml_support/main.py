import vendor_hardware, logistics_hardware, inventory_hardware

if __name__== "__main__":
    # Code from different teams will be calling these functions.
    # Calling them from main for illustration purposes.

    # Vendor team storing their vendor detail.
    vendor_mysql_config = {}
    vendor_mysql_config['max_threads'] = 10
    vendor_mysql_config['port'] = 3307
    vendor_mysql_config['max_conn'] = 200
    vendor_hardware.store_mysql_config(vendor_mysql_config)

    # Vendor team storing the resolv.conf file config of their main server.
    vendor_resolv_config = {}
    vendor_resolv_config['nameserver'] = '127.0.0.53'
    vendor_resolv_config['options'] = 'edns0'
    vendor_hardware.store_resolv_config(vendor_resolv_config)

    # Logistics team storing some configuration of their own.
    logistics_rest_server_config = {}
    logistics_rest_server_config['max_threads'] = 10
    logistics_rest_server_config['port'] = 80
    logistics_rest_server_config['max_listeners'] = 50
    logistics_hardware.store_logistics_rest_server_config(logistics_rest_server_config)
    
    # Inventory team storing their inventory detail.
    inventory_mysql_config = {}
    inventory_mysql_config['max_threads'] = 100
    inventory_mysql_config['port'] = 3306
    inventory_mysql_config['max_conn'] = 10
    inventory_hardware.store_mysql_config(inventory_mysql_config)

    # Read stored configs of vendor team later.
    print('Printing MySQL config of vendor team')
    print(vendor_hardware.read_mysql_config())
    print('Print resolv config of vendor servers')
    print(vendor_hardware.read_resolv_config())

    # Read stored configs of logistics team later.
    print('Print rest server config of logistics team')
    print(logistics_hardware.read_logistics_rest_server_config())
    
    # Read stored configs of inventory team later.
    print('Printing MySQL config of inventory team')
    print(inventory_hardware.read_mysql_config())

