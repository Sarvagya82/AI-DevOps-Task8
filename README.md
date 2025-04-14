# AI-DevOps-Task8
This repository contains the files and steps to deploy a simple scikit-learn Iris classification model as an API endpoint using Docker and Kubernetes (Minikube).

**Key Steps:**

1.  **Trained an AI model:** A Logistic Regression model was trained on the Iris dataset using scikit-learn and saved as `iris_model.joblib`.
2.  **Created a Flask API:** A Python Flask application (`app.py`) was developed to load the trained model and expose a `/` endpoint that accepts flower measurements as JSON input and returns the predicted class.
3.  **Containerized the API:** A `Dockerfile` was created to build a Docker image containing the Flask API, the trained model, and all necessary dependencies.
4.  **Deployed to Kubernetes:** Kubernetes YAML files (`deployment.yaml` and `service.yaml`) were defined to deploy the Docker image to a local Minikube cluster and expose the API via a LoadBalancer service.

**To run this deployment:**

1.  Ensure Docker, Minikube, and Kubectl are installed.
2.  Build and push the Docker image to a container registry (e.g., Docker Hub).
3.  Start the Minikube cluster.
4.  Apply the Kubernetes Deployment and Service YAML files.
5.  Access the API endpoint using the URL provided by Minikube and send POST requests with JSON data to get predictions.
Minikube Url : 192.168.49.2:30881
(eg : curl -X POST -H "Content-Type: application/json" -d '{"sepal_length": 5.9, "sepal_width": 3.0, "petal_length": 4.2, "petal_width": 1.5}' 192.168.49.2:30881)
