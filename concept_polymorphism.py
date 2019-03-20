# Polymorphism

# print polymorphic function
print(1.0)                      # float
print('mystring')               # str
print(['l', 'i', 's', 't'])     # list


# Sample polymorphic function

class Server:
    def __init__(self, name, ip, cpu):
        self.name = name
        self.ip = ip
        self.cpu = cpu

    def ip(self):
        return self.ip


class Switch:
    def __init__(self, name, protocol, ip):
        self.name = name
        self.ip = ip
        self.protocol = protocol

    def ip(self):
        return self.ip


class Storage:
    def __init__(self, ip, capacity):
        self.ip = ip
        self.capacity = capacity

    def ip(self):
        return self.ip


def get_ip(element):
    print(element.ip)


hp = Server('HP', '10.10.1.1', 'Intel')
cisco = Switch ('Cisco', '10GbE', '192.168.1.1')
lsi = Storage ('10.15.5.10', '1TB')


# get_ip() is polymorphic

get_ip(hp)      # print(type(hp))
get_ip(cisco)   # print(type(cisco))
get_ip(lsi)     # print(type(lsi))
