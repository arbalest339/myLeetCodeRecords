while True:
    ip = input()
    ip = ip.split(".")
    ip1 = int(ip[0])<<24
    ip2 = int(ip[1])<<16
    ip3 = int(ip[2])<<8
    ip4 = int(ip[3])
    nip = ip1 | ip2 | ip3 | ip4
    print(nip)

    nip = input()
    nip = int(nip)
    ip[0] = str(nip >> 24 & 255)
    ip[1] = str(nip >> 16 & 255)
    ip[2] = str(nip >> 8 & 255)
    ip[3] = str(nip & 255)
    print(".".join(ip))