# CodeAlpha_Basicnetworksniffer
● Build a Python program to capture network traffic packets. ● Analyze captured packets to understand their structure and content. ● Learn how data flows through the network and the basics of protocols. ● Use libraries like `scapy` or `socket` for packet capturing. ● Display useful information such as source/destination IPs, protocols and payloads.
Network Packet Sniffer (Python)
Project Title
Basic Network Sniffer

Objectives
Capture live network packets.
Analyze packet structure and content.
Understand how data flows through a network.
Learn basics of protocols like TCP, UDP, and ICMP.
Display useful information such as:
Source IP
Destination IP
Protocol type
Ports
Payload
Requirements
Python 3.x
Scapy library
Install Scapy using:

pip install scapy
⚠ Note: Run the script with administrator/root privileges for packet capturing.

How to Run
python packet_sniffer.py
Press Ctrl + C to stop capturing packets.

How It Works
The program uses Scapy's sniff() function to capture packets.
Each packet is passed to process_packet().
The script extracts:
IP layer information
Protocol type (TCP/UDP/ICMP)
Source & destination ports
Payload data
Packet details are printed in readable format.
Learning Outcomes
Understanding packet structure (IP Header, Transport Layer).
Difference between TCP, UDP, and ICMP.
How network traffic flows between devices.
Basic network monitoring concepts.
Important Notes
Use this tool only on networks you own or have permission to monitor.
Unauthorized packet sniffing may be illegal.
