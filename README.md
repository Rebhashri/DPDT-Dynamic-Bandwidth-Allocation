# DPDT Dynamic Bandwidth Allocation

## Demand-Aware Dynamic Bandwidth Allocation for Shared Hostel Networks Using DPDT Traversal

### Overview

Shared hostel networks often experience bandwidth congestion because users have different levels of network demand at different times. A fixed bandwidth allocation may leave some bandwidth unused while other users experience insufficient bandwidth.

This project proposes a Dynamic Bandwidth Allocation approach using DPDT (Diagonal Priority and Demand Traversal) to redistribute unused bandwidth based on the current demand of users.

The system analyzes bandwidth usage at regular time intervals and dynamically reallocates available bandwidth to users with additional demand while maintaining the total network capacity constraint.

---

## Problem Statement

In a shared hostel network, bandwidth is commonly allocated to multiple users based on predefined limits or priorities. However, user demand changes over time.

For example:

- An online interview may require high priority.
- An online class may require medium priority.
- YouTube streaming may require additional bandwidth.
- Gaming may require additional bandwidth.

At the same time, some users may not fully utilize their allocated bandwidth.

The proposed system identifies unused bandwidth and redistributes it to users who require additional bandwidth.

---

## Objectives

The main objectives of this project are:

- To analyze real-time bandwidth usage.
- To identify unused bandwidth.
- To detect additional bandwidth demand.
- To prioritize users based on priority levels.
- To dynamically redistribute available bandwidth.
- To maintain the total network capacity constraint.
- To avoid bandwidth wastage.
- To simulate changing network demand over multiple time intervals.

---

## System Model

The simulation considers a hostel network with a total bandwidth capacity of:

**100 Mbps**

The users are classified into three priority levels:

| User | Activity | Priority |
|------|----------|----------|
| U1 | Online Interview | High |
| U2 | Online Class | Medium |
| U3 | YouTube | Low |
| U4 | Gaming | Low |

The initial bandwidth allocation is:

| User | Initial Allocation |
|------|-------------------|
| U1 | 20 Mbps |
| U2 | 15 Mbps |
| U3 | 30 Mbps |
| U4 | 25 Mbps |

Total initial allocation:

**90 Mbps**

The remaining network capacity can be dynamically utilized based on user demand and available bandwidth.

---

## DPDT Traversal

The proposed DPDT approach traverses the priority levels diagonally:

**High → Medium → Low**

At each priority level, the algorithm:

1. Calculates unused bandwidth.
2. Identifies additional bandwidth demand.
3. Checks the available redistribution pool.
4. Attempts to satisfy the current demand.
5. If sufficient bandwidth is available, the full demand is allocated.
6. If insufficient bandwidth is available, the remaining bandwidth is proportionally distributed among users at that priority level.
7. The algorithm continues to the next priority level.
8. A final capacity check ensures that total allocation does not exceed the network capacity.

---

## Bandwidth Redistribution Process

The redistribution process follows these steps:

```text
Monitor Bandwidth Usage
          ↓
Calculate Unused Bandwidth
          ↓
Create Redistribution Pool
          ↓
Calculate Additional Demand
          ↓
DPDT Priority Traversal
          ↓
High Priority
          ↓
Medium Priority
          ↓
Low Priority
          ↓
Allocate Available Bandwidth
          ↓
Apply Proportional Sharing if Required
          ↓
Check Network Capacity
          ↓
Generate Final Allocation

---

## Simulation Results

The proposed DPDT algorithm was tested using four different time intervals with changing user bandwidth requirements.

The simulation demonstrates that:

- Unused bandwidth is identified dynamically.
- Additional bandwidth demand is calculated for each user.
- Bandwidth is redistributed according to priority and demand.
- High-priority users are processed first.
- When sufficient bandwidth is unavailable, proportional sharing is applied.
- The total allocated bandwidth is maintained within the 100 Mbps network capacity.
- The algorithm successfully adapts to changing bandwidth requirements across different time intervals.

The simulation was implemented in Python.

---

## Technologies Used

- Python
- Visual Studio Code
- GitHub

---

## Project Structure

```text
DPDT-Dynamic-Bandwidth-Allocation/
│
├── ver12.py
└── README.md
