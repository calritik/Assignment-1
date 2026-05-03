# Q1 - Inventory Report API
 
## what does it do?
Fetches all  inventory report between two days from SQLite.
 
---
 
## Tech Stack
| Layer | Technology |
|-------|-----------|
| Framework | FastAPI |
| ORM | SQLAlchemy (Async) |
| Database | SQLite |
| Validation | Pydantic |
| Server | Uvicorn |
 
---
 
## Folder Structure
```
q1_inventory/
├── main.py                   ← App entry point
├── database.py               ← SQLite connection
├── seed_data.py              ← to put test data
├── requirements.txt          ← Dependencies
├── models/
│   └── inventory.py          ← DB Tables (Inventory + InventoryDetails)
├── schemas/
│   └── inventory.py          ← API response format (Pydantic)
├── services/
│   └── inventory_service.py  ← Business logic (date filter query)
└── routers/
    └── inventory.py          ← API endpoint
```
 ## Step-by-Step Setup
 
### Step 1: Create Virtual Environment
```bash
python -m venv venv
```
 
### Step 2: Activate it
```bash
# Windows
venv\Scripts\activate

```
 
### Step 3: Dependencies install
```bash
pip install -r requirements.txt
```
 
### Step 4: Run Server
```bash
uvicorn main:app --reload
```
 
### Step 5: put test data in other terminal
```bash
python seed_data.py
```
 
### Step 6: open Swagger UI 
```
http://127.0.0.1:8000/docs
```
 
---
 
## Test API
 
### Endpoint
```
GET /api/getInventoryDetails
```

# Q2 - Device Config Notification API 
 
## What does it do?
When any device's `config_changed = True` (set by a batch job),
this API sends a JSON notification to a Kafka topic.
A Kafka consumer listens to that topic and alerts the user.
 
---

<img width="1600" height="959" alt="q2" src="https://github.com/user-attachments/assets/92311fe1-8536-4fd3-86a1-5729f94ce2e1" />

 
## Tech Stack
| Layer | Technology |
|-------|-----------|
| Framework | FastAPI |
| ORM | SQLAlchemy (Async) |
| Database | SQLite |
| Messaging | Apache Kafka (aiokafka) |
| Validation | Pydantic |
| Server | Uvicorn |
 
---
 
## Flow
```
Batch Job
   ↓
config_changed = TRUE (updated in SQLite)
   ↓
POST /api/deviceConfigNotification
   ↓
Fetch devices where config_changed = True
   ↓
Kafka Producer → Topic: "device-config-notifications"
   ↓
Kafka Consumer → Prints alert to terminal
```
 
---
 
## Folder Structure
```
q2_device_notification/
├── main.py                    ← App entry point
├── database.py                ← SQLite connection
├── seed_data.py               ← Test data insertion
├── requirements.txt           ← Dependencies
├── models/
│   └── device.py              ← Devices table
├── schemas/
│   └── device.py              ← Request/Response format (Pydantic)
├── services/
│   └── device_service.py      ← Business logic
├── routers/
│   └── device.py              ← API endpoint
└── kafka/
    ├── producer.py             ← Sends JSON message to Kafka
    └── consumer.py             ← Receives message from Kafka
```
 
---
 
## Step-by-Step Setup
 
### Step 1: Start Kafka + Zookeeper via Docker
```powershell
# Zookeeper first
docker run -d --name zookeeper -p 2181:2181 zookeeper
 
# Then Kafka
docker run -d --name kafka -p 9092:9092 -e KAFKA_ZOOKEEPER_CONNECT=host.docker.internal:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -e KAFKA_BROKER_ID=1 -e KAFKA_LOG_DIRS=/var/lib/kafka/data confluentinc/cp-kafka:7.3.0
```
 
### Step 2: Verify both containers are running
```powershell
docker ps
```
Both `zookeeper` and `kafka` should show `Up` status.
 
### Step 3: Install dependencies
```powershell
pip install -r requirements.txt
```
 
### Step 4: Open 3 separate terminals
 
**Terminal 1 — Start the server:**
```powershell
uvicorn main:app --reload
```
 
**Terminal 2 — Start the Kafka consumer:**
```powershell
python kafka/consumer.py
```
 
**Terminal 3 — Insert test data:**
```powershell
python seed_data.py
```
 
### Step 5: Open Swagger UI
```
http://127.0.0.1:8000/docs
```
 
---

# Q3 - Posts Pagination API 
 
## Problem Statement
A social networking giant's API was timing out due to huge dataset.
`GET /getPostsUploaded` was fetching millions of rows at once — causing DB timeout.
 
## Solution
Pagination using `LIMIT` and `OFFSET` — fetch only the requested page of records.
Also added DB Indexes on `post_dt` and `post_by` for faster queries.
 
---

<img width="1600" height="961" alt="q3" src="https://github.com/user-attachments/assets/ff368a39-876d-4493-853f-113dd266dc26" />

 
## Tech Stack
| Layer | Technology |
|-------|-----------|
| Framework | FastAPI |
| ORM | SQLAlchemy (Async) |
| Database | SQLite |
| Optimization | Pagination (LIMIT + OFFSET) + DB Indexes |
| Validation | Pydantic |
| Server | Uvicorn |
 
---
 
## Folder Structure
```
q3_posts_pagination/
├── main.py                  ← App entry point
├── database.py              ← SQLite connection
├── seed_data.py             ← Test data insertion
├── requirements.txt         ← Dependencies
├── models/
│   └── post.py              ← Posts table + DB Indexes
├── schemas/
│   └── post.py              ← Paginated response format
├── services/
│   └── post_service.py      ← Pagination logic (OFFSET + LIMIT)
└── routers/
    └── post.py              ← API endpoint
```
 
---
## Step-by-Step Setup
 
### Step 1: Install dependencies
```powershell
pip install -r requirements.txt
```
 
### Step 2: Start the server
```powershell
uvicorn main:app --reload
```
 
### Step 3: Insert test data (separate terminal)
```powershell
python seed_data.py
```
 
### Step 4: Open Swagger UI
```
http://127.0.0.1:8000/docs
```
 
---
