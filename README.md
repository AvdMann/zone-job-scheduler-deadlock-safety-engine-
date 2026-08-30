# Zone Job Scheduler, Deadlock-Safety Engine & Cloud-IoT Deployment Blueprint

## Repository Contents

### Part 1

- jobs.py
- scheduling_algorithms.py
- round_robin.py
- priority_scheduling.py
- peterson_demo.py
- bankers_algorithm.py
- memory_translation.py
  
# Part 2 Deployment Blueprint

See the deployment blueprint here:

docs/architecture_blueprint.md

---

# How to Run Part 1

## FCFS, SJF and SRTF

```bash
python scheduling_algorithms.py
```

## Round Robin (Quantum 3 and Quantum 6)

```bash
python round_robin.py
```

## Priority Scheduling

```bash
python priority_scheduling.py
```

## Peterson's Algorithm Demo

```bash
python peterson_demo.py
```

## Banker's Algorithm

```bash
python bankers_algorithm.py
```

## Paging and Segmentation Translation

```bash
python memory_translation.py
```

---

# Part 2 Deployment Blueprint

See the deployment blueprint here:

docs/architecture_blueprint.md

---

# Project Overview

This project implements:

- FCFS Scheduling
- SJF Scheduling
- SRTF Scheduling
- Round Robin Scheduling
- Priority Scheduling with Aging
- Peterson's Algorithm
- Banker's Algorithm
- Paging Translation
- Segmentation Translation

The deployment blueprint describes how the Part 1 scheduler and safety engine can be deployed securely in a Smart City cloud and IoT environment.
