# SYN Flood Attack – Network Security Project

This is a simple educational project that demonstrates how a **SYN Flood attack** works using **Python** and **Scapy**.

## 📌 Project Overview

A SYN Flood is a type of Denial-of-Service (DoS) attack that exploits the **TCP three-way handshake** mechanism. In this attack, the attacker sends a large number of TCP/SYN packets with spoofed IP addresses to the target server, overwhelming its resources and preventing it from handling legitimate connections.

This project was implemented as part of a university **Network Security** course.

---

## 🚀 Tools Used
- 🐍 Python
- 🧪 Scapy
- 🐙 Kali Linux (attacker)
- 💻 Windows 10 (victim)
- 🧠 Wireshark (traffic monitoring)
- 📊 Task Manager (performance observation)

---

## 🧠 How it Works

1. The attacker sends a flood of **SYN** packets to the target.
2. The server responds with **SYN-ACK** but never receives the final ACK.
3. This fills the connection queue and eventually leads to service degradation.

---

## 🧪 Demonstration Steps

- Monitor normal CPU and Ethernet performance.
- Run the Python SYN Flood script on the attacker machine.
- Observe real-time traffic using Wireshark.
- Watch the victim machine slow down under attack.
- Apply mitigation strategies (Firewall, IDS/IPS, Load Balancer).

---

## 💻 How to Run

```bash
# Run this command from your Kali Linux machine
sudo python3 syn_flood_attack.py
