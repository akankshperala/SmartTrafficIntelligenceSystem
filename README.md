# 🚦 Smart Traffic Intelligence System (UMIP)

A Smart Traffic Intelligence System built using **Python** and **SUMO (Simulation of Urban Mobility)** to simulate urban traffic, monitor vehicle movement, and analyze congestion across a city road network.

---

## Features

-  Automatic traffic route generation
-  SUMO-based traffic simulation
-  Real-time congestion analytics
-  Vehicle tracking using TraCI
-  Road-wise congestion analysis
-  Modular architecture for simulation and analytics

---

## Tech Stack

- Python 3.x
- SUMO (Simulation of Urban Mobility)
- TraCI
- sumolib

---

## Project Structure

```
UMIP/
│
├── analytics/
│   └── analytics_engine.py
│
├── core/
│   └── cache/
│       └── vehicle_tracker.py
│
├── network/
│   └── maps/
│       └── grid_3x3/
│           ├── config/
│           ├── generated/
│           ├── routes/
│           └── scripts/
│
├── simulator/
│   ├── config.py
│   ├── simulation.py
│   └── traci_manager.py
│
├── run.py
└── requirements.txt
```

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd UMIP
```

---

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` yet:

```bash
pip install traci sumolib
```

---

### 3. Install SUMO

Download SUMO from

https://sumo.dlr.de/docs/Downloads.php

Install it normally.

---

### 4. Configure Environment Variables

Create a new environment variable

```
SUMO_HOME
```

Set its value to

```
C:\Program Files (x86)\Eclipse\Sumo
```

(or wherever SUMO is installed)

Add the following to your **PATH**

```
%SUMO_HOME%\bin
```

```
%SUMO_HOME%\tools
```

Restart VS Code or your terminal after updating the environment variables.

---

## Running the Project

Execute

```bash
python run.py
```

The application will

- Generate vehicle routes
- Launch the SUMO simulation
- Connect to SUMO using TraCI
- Run the simulation
- Track vehicle movement
- Compute congestion statistics

---

## Simulation Workflow

```
Generate Road Network
          │
          ▼
Generate Vehicle Routes
          │
          ▼
Launch SUMO
          │
          ▼
Connect using TraCI
          │
          ▼
Run Simulation
          │
          ▼
Track Vehicles
          │
          ▼
Analyze Traffic
          │
          ▼
Display Congestion Metrics
```

---

## Configuration

Simulation settings can be modified in

```
simulator/config.py
```

Example

```python
SUMO_GUI = True

SUMO_CONFIG = "network/maps/grid_3x3/config/simulation.sumocfg"

STEP_LENGTH = 1.0

MAX_STEPS = 10000
```

---

## Requirements

- Python 3.10+
- SUMO 1.27+
- TraCI
- sumolib

---

## Authors : Akanksh Perala, Keerthi Reddy Gangu

Developed as part of the **UMIP Smart Traffic Intelligence System** project.
