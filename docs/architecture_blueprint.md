# Cloud, Security & IoT Deployment Blueprint

## Overview

This blueprint describes deployment of the Part 1 Zone Job Scheduler, Deadlock-Safety Engine, Banker's Algorithm module, Peterson's Algorithm demonstration, and memory-management components within a Smart City cloud platform.

---

# 1. Distributed Architecture and Communication Plan

## Selected Architecture

Client-Server Architecture

### Justification

- Centralized monitoring through a Smart City Operations Dashboard.
- Improved scalability by adding additional zone controllers.
- Better transparency because all processing status is visible at the dashboard.
- Easier administration and security management.

## Communication Plan

### Real-Time Public Safety Alert

- Communication Type: Synchronous
- Protocol: HTTPS

Reason:
Emergency alerts require immediate acknowledgement and reliable delivery.

### Daily Sensor Log Upload

- Communication Type: Asynchronous
- Protocol: MQTT

Reason:
Large log uploads do not require immediate responses and can be queued.

---

# 2. VPC Network Boundary Design

A single VPC with three isolated subnets:

- Zone-A Subnet
- Zone-B Subnet
- Zone-C Subnet

Benefits:

- Logical isolation
- Simplified network management
- Independent security policies

### Control Enforcing Isolation

Security Group Rules

Example:

- Deny inbound traffic from Zone-B subnet to Zone-A subnet.
- Deny inbound traffic from Zone-C subnet to Zone-B subnet.

---

# 3. Network Security Objectives

| Objective | Control |
|-----------|----------|
| Protect Sensitive Data | AES-256 Encryption |
| Authentication | Multi-Factor Authentication |
| Authorization | Role-Based Access Control |
| Prevent Cyber Attacks | Firewall Rules |
| Secure Communication | TLS 1.3 |
| Ensure Availability | Load Balancing |

---

# 4. IAM Roles

| Role | Permissions |
|--------|------------|
| Zone Operator | Submit and monitor jobs |
| Dashboard Administrator | Full platform administration |
| Security Auditor | Read-only access to logs and reports |

---

# 5. Data Protection Map

## Data At Rest

Example:
JOBS list stored on cloud storage.

Protection:
AES-256 Encryption

## Data In Transit

Example:
Alert transmission from zone controller to dashboard.

Protection:
TLS Encryption

## Data In Use

Example:
Banker's Algorithm safety checks executed in memory.

Protection:
Process isolation and access control.

---

# 6. IoT Connectivity

| Device | Communication Technology |
|----------|------------------------|
| Traffic Camera | 5G |
| Environmental Sensor | LoRaWAN |
| Public Safety Wearable | NB-IoT |

---

# 7. IoT Architecture Layers

### Physical Environment

Roads, intersections, public infrastructure.

### Perception Layer

Traffic cameras, sensors, wearables.

### Gateway Layer

Zone gateways collecting sensor data.

### Network Communication Layer

HTTPS, MQTT, TCP/IP networking.

### Cloud Platform Layer

Zone Job Scheduler and Deadlock-Safety Engine from Part 1.

### Application Layer

Smart City Operations Dashboard.

---

# 8. Threats and Mitigations

| Threat | Mitigation |
|----------|-----------|
| Unauthorized Access | MFA and RBAC |
| IoT Device Spoofing | Device Authentication Certificates |
| DDoS Attacks | Firewall and Load Balancers |

---

# Conclusion

The architecture provides a secure, scalable and manageable deployment platform for the Zone Job Scheduler, Deadlock-Safety Engine and Smart City IoT services.
