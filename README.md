# Application-Monitoring-Dashboard

This repository contains the code and setup for the **Application Monitoring Dashboard** project. 

---

## 🗓️ Week 1: Setup and Initial Configuration


---

### 📦 Prerequisites

Before running the project, ensure you have pip installed, if not then follow the below 2 commands:
```bash
sudo apt update 
sudo apt install python3 python3-pip python3-venv -y 
```
To install Kafka and fastapi, run the below in your root directory:
```bash
python3 -m venv env 
source env/bin/activate 
pip install fastapi uvicorn kafka-python 
```
---

### 🚀 Running the Week 1 Setup

Follow these steps to get the project running:

1. **Clone the repository:**

    First, clone the repository to your local machine:

    ```bash
    git clone https://github.com/HannahAlex004/Application-Monitoring-Dashboard.git
    cd Application-Monitoring-Dashboard
    ```

2. **Install dependencies:**

   Mentioned in prequisites.

3. **Check the setup:**

    1. Successsful API Responses and Errors [200 OK nand 404/500]
    ```bash
    python3 -m uvicorn app:app --reload
    ```
    Open http://localhost:8000/docs in a browser. 
    Click on endpoints like /users/1, /error-test, etc, to see if they work. 
    
    2. Continuous random API calls with status codes
    ```bash
    python3 load_test.py
    ```
    Show real-time logs: 
            Hit /users/1 → Status: 200 
            Hit /error-test → Status: 500 
    
    3. Kafka running in Docker
    Kafka and Zookeeper containers running. 
    Topics (api-logs, error-logs) created.
    Check running containers:
     ```bash
    docker ps
    ```
    List Kafka topics:
     ```bash
    docker exec -it kafka_kafka_1 bash 
    kafka-topics --list --bootstrap-server localhost:9092 
    exit 
    ```

    4. Kafka Producer Logging API Requests
    ```bash
    docker exec -it kafka_kafka_1 bash 
    kafka-console-consumer --topic api-logs --bootstrap-server localhost:9092
    ```

    5. Dockerized setup
    ```bash
    cat docker-compose.yml
    docker-compose down && docker-compose up-d
    curl http://localhost:8000/
    docker-compose logs
    ```

## 🗓️ Week 2: Kafka Consumer and MySQL Integration
---

### 📦 Prerequisites
You should have the following prerequisites installed and set up:

- **Docker**: For running MySQL and Kafka.
- **Kafka Consumer**: Python script to read from Kafka and insert logs into MySQL.
- **MySQL Database**: For storing the logs.
---
### 🚀 Steps to Run Week 2

#### 1. Ensure MySQL is Running in Docker

Make sure your **MySQL database** is set up and running using Docker. You can start it using:

```bash
docker-compose up -d
```
Check the containers are running by listing active containers:
```bash
docker ps
```
#### 2. Create the logdb Database in MySQL

Make sure your **MySQL database** is set up and running using Docker. 

### 3. Run the Kafka Consumer Script
```bash
python3 consumer.py
```
Expected Output:
```bash
MySQL connection successful.
Starting consumer...
```
### 4. Simulate Load Test
```bash
python3 load_test.py
```
### 5. Verify logs in MySQL
```bash
USE logdb;
SELECT * FROM logs;
```
## 📊 Week 3 – Grafana Dashboard Setup
---

### 📦 Prerequisites
You should have the following prerequisites installed and set up:

- **Docker** and **Docker Compose** installed
- **MySQL** running (refer Week 2 setup)
- **Kafka + Kafka consumer** script already pushing data to logdb
- **Grafana** image pulled (or installed)

---
### 🚀 Steps to Run Week 3

#### 1. Ensure MySQL is Running in Docker
If the MySQL and Kafka containers are already running, start the updated system using

``bash
docker-compose -f docker-consumer.yml up -d
```

Start all the required three containers using:

```bash
docker-compose up -d
```
Check the containers are running by listing active containers:
```bash
docker ps
```
#### 2. Configure Grafana
Make sure your **MySQL database** is set up and running using Docker. 
- 1.	Access Grafana at
     ```bash
     http://localhost:3000
     ```
  2. Login with admin/admin (you'll be prompted to change the password)
  3. Add MySQL as datasource -
     - Click "Configuration" (gear icon) > "Data Sources"
     - Click "Add data source"
     - Select MySQL
     - Configure with:
       - Name: MySQL
       - Host: mysql:3306
       - Database: logdb
       - User: root
       - Password: xxx(your sql pass)
       - TLS/SSL Mode: Disable
     - Click "Save & Test"
  4. Creating Dashboard in Grafana:
     - Log in  to Grafana,
       - go to ```bash http://localhost:3000 ```
       - Login with admin/admin (change password if prompted).
     - Create a new Dashboard
       - Look for the "Dashboards" icon (four squares) in the left menu.
       - Click "New" (button on the top-right).
       - Select "New Dashboard".
     - Add a panel
       You’ll see an empty dashboard.
       - Click "Add visualization" (or "Add panel").
         Adding Your First Panel (Example: Request Count)
       - Select Data Source, Choose MySQL (the one you configured earlier).
       - Switch to "Code" Mode (SQL)
       - Click the "Edit SQL" button (or select "SQL" from the query type dropdown).
       - Paste the SQL Query
   5. Visualization Settings :
      - Under "Visualization" (right sidebar), select "Bar chart".
      - Set a Panel title (e.g., "Request Count by Endpoint").
      - Save the Panel: Click "Apply" (top-right).
   6. The sql queries to use  to create panels,
      - Request Count per Endpoint
        ```bash
        SELECT url AS metric,COUNT(*) AS count
        FROM logs
        GROUP BY url
        ORDER BY count DESC
        ```
      - Response Time Trends
        ```bash
        SELECT timestamp AS time, duration AS value,url AS metric
        FROM logs
        ```
      - Most Frequent Errors
        ```bash
        SELECT url AS metric,COUNT(*) AS error_count
        FROM logs
        WHERE error = 1
        GROUP BY url
        ORDER BY error_count DESC
        ```
      - Real-time Logs Feed
        ```bash
        SELECT url AS metric,COUNT(*) AS error_count
        FROM logs
        WHERE error = 1
        GROUP BY url
        ORDER BY error_count DESC
        ```
    Add more panels if needed.

