Neural Collaborative Filtering Recommendation System (MLOps with GCP, Jenkins, DVC, Docker, Flask)
This project implements a Neural Collaborative Filtering (NCF)-based recommendation system using a full MLOps pipeline, powered by:

Google Cloud Platform (GCP): Buckets, GKE (Google Kubernetes Engine)

Jenkins: Continuous Integration & Deployment (CI/CD)

DVC: Data versioning

Comet ML: Experiment tracking

Docker-in-Docker (DinD): For Jenkins job containerization

Flask API: Model serving via endpoint

Pipeline Overview
1. Data Ingestion
Downloads raw data from GCP buckets

Uses Google service account for authentication

Data stored under DVC for version control

2. Data Processing
Preprocessing, filtering, and splitting

Prepares user-item interaction matrix

3. Model Training
Neural Collaborative Filtering with TensorFlow

Tracks metrics using Comet ML

4. Model Serving
Exposed as REST API using Flask

Deployed to 2 Pods on Google Kubernetes Engine (GKE)

Externally accessible GKE Endpoint for inference

5. CI/CD with Jenkins
Jenkins containerized with Docker-in-Docker (DinD)

Stages: Git clone → Virtualenv → DVC pull → Docker build → Push to GCR → Deploy to GKE → Run training container






![Screenshot](https://github.com/jothsnapraveena/Recommendation-System-MLOPS/blob/master/Screenshot%202025-03-19%20221627.png?raw=true)
![Screenshot](https://github.com/jothsnapraveena/Recommendation-System-MLOPS/blob/master/Screenshot%202025-03-22%20141643.png?raw=true)


