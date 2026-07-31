Multi-Tier Enterprise Application Infrastructure

Overview
The project presents a secure multi-tiered application infrastructure that was designed and built on Amazon Web Services. The application is deployed on a public-facing frontend, private backend, and private database servers. The application consists of an NGINX frontend web server, a flask backend API, and Amazon RDS MySQL database interconnected with VPC, security groups, and NAT Gateway.

Features
• Public frontend application hosted on Amazon EC2 web server
• Private backend API hosted on Amazon EC2 web server
• Private Amazon RDS MySQL database

• VPC isolated subnets
• Internet gateway and route tables
• Network Address Translation (NAT) gateway
• IAM users and Cloudwatch monitoring

• Frontend to backend to database communication
AWS Services
Amazon EC2, Amazon VPC, Public and Private Subnets, Internet Gateway, NAT Gateway, Route Tables, Security Groups, Amazon RDS MySQL, IAM, Amazon CloudWatch.
Technologies
HTML, CSS, JavaScript, Python, Flask, PyMySQL, Nginx, Ubuntu, MySQL.

Project’s Workflow
1. The user sends an HTTP request by filling out the form on the website.
2. The frontend NGINX server responds to the request and routes it to the backend flask server.
3. The flask server receives the request and saves the information in the database.
4. The database on Amazon RDS MySQL stores the request data.
5. The user receives a success message on the frontend.
The Project Structure
frontend/
backend/
screenshots/
README.md