# 🖥️ Server Health Monitor

A lightweight, containerized Python utility designed to monitor system resources (CPU and Memory) and trigger automated alerts when usage exceeds defined thresholds. 

This project demonstrates core DevOps principles including infrastructure monitoring, Python scripting, dependency management, and Docker containerization.

## 🚀 Features
* **Real-Time Monitoring:** Captures CPU and RAM usage using the `psutil` library.
* **Automated Alerting:** Logs a timestamped warning to `system_alerts.log` if resource usage exceeds 80%.
* **Containerized:** Fully packaged with Docker for consistent, isolated execution across any environment.

## 🛠️ Tech Stack
* **Language:** Python 3.9
* **Libraries:** `psutil`, `datetime`
* **Containerization:** Docker

---

## 💻 How to Run Locally (Python)

**1. Clone the repository:**
```bash
git clone [https://github.com/subashsakthi279/server-health-monitor.git](https://github.com/subashsakthi279/server-health-monitor.git)
cd server-health-monitor
