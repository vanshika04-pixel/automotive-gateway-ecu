Automotive Multi-ECU Vehicle Network Simulator
Overview

This project simulates the electronic backbone of a modern vehicle.
It models how multiple Electronic Control Units (ECUs) communicate through a central Gateway ECU using CAN and Automotive Ethernet concepts, including cybersecurity firewalling and ADAS collision detection.

The architecture is inspired by real Tier-1 automotive supplier designs (Bosch, Continental, ZF, BMW, Audi).

System Architecture
Engine/Body ECUs (CAN)
        │
        ▼
   Gateway ECU  ───►  Automotive Ethernet Backbone
        │
        ├──► ADAS Camera ECU (collision detection)
        │
        └──► Firewall ECU (cybersecurity filtering)

Implemented ECUs
ECU	Description
Gateway ECU	Converts CAN messages to Ethernet packets
ADAS ECU	Simulates front camera object detection
Firewall ECU	Blocks malicious CAN frames
Diagnostics ECU	Logs system activity
Technologies Used

python

CAN bus concepts

Automotive Ethernet concepts

Cybersecurity hashing (SHA-256)

ECU architecture modeling

Linux/Windows compatible

How to Run
python gateway.py
python adas_ecu.py
python firewall_ecu.py

Skills Demonstrated

In-vehicle networking (CAN / Ethernet)

Automotive ECU architecture

ADAS system logic

Automotive cybersecurity principles

Diagnostics and validation logic

Author

Vanshika Saxena
M.Sc. Media Engineering – TU Ilmenau
Automotive Embedded & Vehicle Network Engineering
