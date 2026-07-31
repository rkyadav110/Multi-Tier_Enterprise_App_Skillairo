# Multi-Tier Enterprise Application Infrastructure

This project is an implementation of a secure multi-tiered application infrastructure on AWS. The application is deployed on AWS using a public frontend, private backend, and private database. The application consists of an Nginx-powered frontend, a Flask API backend, and an Amazon RDS MySQL database, connected through VPC, security groups, and a NAT Gateway.

## Features
- Public frontend (Nginx)
- Private backend (Flask API)
- Private database (Amazon RDS)
- Isolated networks via VPC
- Route tables, internet gateway, and NAT gateway
- IAM users
- CloudWatch monitoring
- Frontend to backend to database data flow

## AWS Services
- Amazon EC2
- Amazon VPC
- Subnets
- Internet Gateway
- NAT Gateway
- Route tables
- Security groups
- Amazon RDS (MySQL)
- IAM
- CloudWatch

## Technologies
- HTML
- CSS
- JavaScript
- Python
- Flask
- PyMySQL
- Nginx
- Ubuntu
- MySQL

## Project Workflow
1. A user sends an HTTP POST request to the application’s frontend (Nginx).
2. Nginx routes the request to the backend API.
3. The backend processes the request and stores the data in the database.
4. The database returns a response to the backend, which in turn relays it to the frontend.
5. The frontend displays the result of the operation to the user.

The project structure is as follows:
```
frontend/
backend/
screenshots/
README.md
```
