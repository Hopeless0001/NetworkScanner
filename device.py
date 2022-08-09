from datetime import datetime
from colors import r, g, n

class Device(object):
    def __init__(self, mac, ip, network_name, data={}):
        self.mac = mac
        self.ip = ip
        self.network_name = network_name

    def to_list(self):
        color = g

        mac = '{}{}{}'.format(color, self.mac, n)
        ip = '{}{}{}'.format(color, self.ip, n)
        network_name = '{}{}{}'.format(color, self.network_name, n)
        return [mac, ip, network_name]

    def to_string(self):
        return 'Log: {} \n\t Mac Address: {} \n\t Name in network: {}'.format(datetime.now(), self.mac, self.network_name)
