# Mini_side_project
# 🌦 Weather Monitoring Stack (Prometheus + Grafana + MCP Server)

This project demonstrates a complete monitoring pipeline using:

- Prometheus (metrics collection)
- Grafana (visualization)
- Python MCP Server (metrics exporter)
- Docker & Docker Compose (container orchestration)
- OpenWeather API (external data source)

The goal of this project is to learn and implement real-world monitoring architecture using modern DevOps tools.

---

## 🚀 Project Architecture

OpenWeather API  
        ↓  
weather_service (Python MCP Server)  
        ↓  
/metrics endpoint (Port 8000)  
        ↓  
Prometheus (Port 9090)  
        ↓  
Grafana (Port 3000)  

---

## 🧩 Tech Stack

- Python 3.12
- Prometheus
- Grafana
- Docker
- Docker Compose
- OpenWeather API
- Prometheus Client Library (Python)

---

## 🔌 Ports Used

- **8000** → Weather MCP Server (/metrics endpoint)
- **9090** → Prometheus server UI
- **3000** → Grafana dashboard UI

---

## ⚙️ How It Works

1. The Python MCP server fetches temperature data from OpenWeather API.
2. It exposes the metric `india_temperature_celsius` on `/metrics`.
3. Prometheus scrapes this endpoint at regular intervals.
4. Grafana connects to Prometheus and visualizes the time-series data.

---

## 📦 Running the Project

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
