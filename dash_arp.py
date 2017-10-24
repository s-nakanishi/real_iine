from scapy.all import sniff, ARP
 
def arp_monitor_callback(pkt):
  if ARP in pkt and pkt[ARP].op in (1,2):
    return pkt.sprintf("%ARP.hwsrc% | %ARP.psrc%")
 
print(sniff(prn=arp_monitor_callback, filter="arp", store=0))
