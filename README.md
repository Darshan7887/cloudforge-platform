🚀 CloudForge Microservices Platform

A production-style Dockerized microservices architecture built using FastAPI and PostgreSQL with centralized JWT authentication and service-to-service validation.

🏗️ Architecture Overview

CloudForge consists of independent backend services communicating over Docker's internal network.

Services

🔐 Auth Service

User registration & login

JWT token generation

Centralized token validation endpoint

Secure password hashing

👤 User Service

Profile management

Protected endpoints

Service-to-service authentication via Auth Service

🗄 PostgreSQL

Containerized database

Persistent Docker volume

Shared across services

🔐 Authentication Flow
Client
│
├── Login Request
│ │
│ └── Auth Service
│ └── Returns JWT
│
└── Protected Request (with JWT)
│
└── User Service
│
└── Internal HTTP Call
→ Auth Service (/validate-token)
└── Validates JWT
Unlike typical demo projects, JWT validation is centralized inside the Auth Service — preventing logic duplication across services.

🛠️ Tech Stack

FastAPI

PostgreSQL

Docker & Docker Compose

SQLAlchemy

JWT (PyJWT)

Requests (Service-to-service communication)

Pydantic

📂 Project Structure
cloudforge-microservices/
│
├── docker-compose.yml
├── services/
│   ├── auth-service/
│   │   ├── app/
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   └── user-service/
│       ├── app/
│       ├── Dockerfile
│       └── requirements.txt


🚀 Running Locally
1️⃣ Clone the Repository
git clone https://github.com/Darshan7887/cloudforge-platform.git
cd cloudforge-microservices
2️⃣ Start the Services
docker compose up --build

🌐 Service Endpoints
Service	URL
Auth Service	http://localhost:8001/docs

User Service	http://localhost:8002/docs
🔎 Features Implemented

Dockerized microservices architecture

Centralized JWT authentication

Service-to-service token validation

Internal Docker DNS networking

Persistent PostgreSQL storage

Clean dependency injection pattern

Timeout-based resilient token verification

🧠 Engineering Highlights

Separation of concerns between services

No duplicated authentication logic

Environment-driven configuration

Production-style container orchestration

Clean modular backend structure

📈 Future Enhancements

API Gateway layer (Nginx)

Role-Based Access Control (RBAC)

Redis caching

Prometheus + Grafana monitoring

Kubernetes deployment (EKS/Minikube)

CI/CD pipeline (GitHub Actions)

🎯 Purpose

This project was built to deeply understand:

Distributed authentication systems

Docker networking

Microservice communication patterns

Debugging container orchestration issues

Production-grade backend structuring

👨‍💻 Author

Darshan Nerkar
B.Tech IT | Aspiring Cloud & DevOps Engineer
