from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst
        print(f"Packet: {ip_src} -> {ip_dst}")

        # Add conditions to detect suspicious activity (e.g., specific IPs or protocols)
        # Example: detect if packet is sent to an unknown external IP
        if ip_dst not in ['trusted_ip_1', 'trusted_ip_2']:  # replace with known trusted IPs
            print(f"Suspicious activity detected: {ip_src} -> {ip_dst}")

# Start monitoring network packets
print("Monitoring network traffic...")
sniff(filter="ip", prn=packet_callback, store=0)

