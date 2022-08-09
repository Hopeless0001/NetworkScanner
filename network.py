from nmap import PortScanner

class Network(object):
    def __init__(self):
        self.ip_default = '192.168.1.1'
        self.ip = input('Please input network IP (press return for ' + self.ip_default + '):\n')
        
    def get_devices(self):
        if len(self.ip) >= 1:
            network_to_scan = self.ip + '/24'
        else:
            network_to_scan = self.ip_default + '/24'

        scanner = PortScanner()
        print('Scanning {}...'.format(network_to_scan))
        scanner.scan(hosts=network_to_scan, arguments='-sn') 
        device_list = [(device, scanner[device]) for device in scanner.all_hosts()]
        return device_list
