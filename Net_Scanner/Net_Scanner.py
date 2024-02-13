import scapy.all as scapy
import optparse

def Options():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-i","--ipadress",dest="ip_adress",help="Type IP adress")

    (user_input,arguments)=parse_object.parse_args()
    if not user_input.ip_adress:
        print("Type IP adress!!")
    return user_input

def Request_Scan(ip):
    arp_request= scapy.ARP(pdst=ip)

    broadcasting=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    combined_packed=broadcasting/arp_request

    (answered_ones,unanswered_ones)=scapy.srp(combined_packed,timeout=1)
    answered_ones.summary()


user_ip_adress=Options()
Request_Scan(user_ip_adress.ip_adress)