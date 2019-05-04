with open('ip_and_mac_addresses.txt') as data_from_net:
    devices_dict = {}
    for device in data_from_net:
        device = device.rstrip().split()
        devices_dict[device[0]] = dict(mac = device[1], ip = device[2])




