from getmac import get_mac_address
from prettytable import PrettyTable

import datetime

from device import Device
from network import Network

import sys
def create_device_list(devices):
    unknown_devices = []

    for host, info in devices:
        device = Device(info['mac'], host, info['hostnames'][0]['name'])
        unknown_devices.append(device)

    return {'unknown': unknown_devices}

if __name__ == '__main__':

    network = Network()

    try:
        startTime = datetime.datetime.now()
        devices = network.get_devices()
    except KeyboardInterrupt:
        print('You stopped scanning.')
        sys.exit()

    for host, info in devices:
        info['mac'] = get_mac_address(ip=host)

    data = create_device_list(devices)
    log_text = ''

    table = PrettyTable()
    table.field_names = ["MAC ADDRESS", "IP", "NAME IN NETWORK"]
    for device in data['unknown']:
        table.add_row(device.to_list()[:3])
        log_text += '{}\n'.format(device.to_string())
    
    print('Unknown Devices\n{}'.format(table))
    endTime = datetime.datetime.now()
    finalTime = endTime - startTime
    print('Scanning completed in {} seconds'.format(finalTime.seconds))