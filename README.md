# Cloud-Based Student Task Manager

A secure cloud-hosted Student Task Manager web application developed using Flask and deployed on AWS cloud infrastructure. The project implements secure authentication, role-based access control, task management, HTTPS deployment, monitoring, security hardening, automated backups, and cloud-based infrastructure integration.

---

# Live Deployment

https://3.110.85.242.nip.io

---

# Project Features

## Application Development

- User Registration and Login
- Role-Based Access Control (User/Admin)
- Task CRUD Operations
- Admin Dashboard
- Flask Web Application
- Responsive UI Design

---

# AWS Cloud Infrastructure

- AWS EC2 Ubuntu Server Deployment
- AWS RDS MySQL Integration
- AWS S3 Backup Storage
- AWS CloudWatch Monitoring
- Security Groups Configuration
- HTTPS Deployment using Let's Encrypt SSL

---

# Linux Administration

- Ubuntu Server Configuration
- Nginx Reverse Proxy
- Gunicorn Application Server
- SSH Hardening
- Key-Based Authentication
- Fail2ban Intrusion Prevention
- systemd Service Management
- Cron-based Automation
- Log Rotation using logrotate

---

# Cyber Security Features

- bcrypt Password Hashing
- Flask-Login Session Authentication
- API Rate Limiting using Flask-Limiter
- Failed Login Tracking
- Security Headers
- Content Security Policy (CSP)
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
- HTTPS SSL/TLS Encryption
- Brute-force Protection using Fail2ban
- SQL Injection Protection using SQLAlchemy ORM

---

# Monitoring & Logging

- AWS CloudWatch Logs
- CPU Monitoring
- Memory Monitoring
- Disk Monitoring
- Failed Login Monitoring
- Uptime Monitoring using UptimeRobot
- Nginx Log Monitoring
- Security Monitoring

---

# Technology Stack

## Backend

- Python
- Flask
- SQLAlchemy
- Flask-Login
- Flask-Bcrypt
- Flask-Limiter

## Database

- MySQL (AWS RDS)
- SQLite (Local Development)

## Cloud & Infrastructure

- AWS EC2
- AWS RDS
- AWS S3
- AWS CloudWatch

## Deployment

- Gunicorn
- Nginx
- Docker
- systemd

## DevOps

- Git
- GitHub

---

# Cloud Architecture

```text
Client Browser
      ↓
HTTPS SSL/TLS
      ↓
Nginx Reverse Proxy
      ↓
Gunicorn
      ↓
Flask Application
      ↓
AWS RDS MySQL
```

---

# Security Architecture

Implemented security protections include:

- HTTPS enforcement
- Content Security Policy (CSP)
- Secure security headers
- API rate limiting
- Failed login monitoring
- Brute-force protection
- bcrypt password hashing
- Secure session authentication
- SQL Injection prevention
- Role-Based Access Control

---

# Deployment Workflow

## Local Development

```bash
python app.py
```

---

## Production Deployment

```bash
git pull
sudo systemctl restart student
sudo systemctl restart nginx
```

---

# Docker Deployment

```bash
docker compose up -d --build
```

---

# Local Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/student-task-manager.git
```

## Open Project

```bash
cd student-task-manager
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

---

# Production URL

https://3.110.85.242.nip.io

---

# Monitoring

- AWS CloudWatch
- UptimeRobot
- Fail2ban
- Nginx Logs
- Failed Login Logs

---

# Author

Jithu Dhanapalan

---

# License

Educational Project