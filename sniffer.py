from scapy.all import sniff, IP, TCP, UDP, ICMP

def process_packet(packet):
    print("="*50)

    if IP in packet:
        ip_layer = packet[IP]

        print("Source IP      :", ip_layer.src)
        print("Destination IP :", ip_layer.dst)

        # Identify protocol
        if packet.haslayer(TCP):
            print("Protocol       : TCP")
        elif packet.haslayer(UDP):
            print("Protocol       : UDP")
        elif packet.haslayer(ICMP):
            print("Protocol       : ICMP")
        else:
            print("Protocol       : Other")

        # Show payload if exists
        if packet.payload:
            print("Payload        :", bytes(packet.payload))

def start_sniff():
    print("Starting Network Sniffer...")
    sniff(prn=process_packet, store=False)

start_sniff()
