<h1>Doctor FOOD</h1>
Doctor FOOD is a web application built using Flask that helps users keep track of their food intake and make healthier food choices. This README file provides a guide on how to deploy the application both locally and on the cloud using Azure pipelines.
<h2>Creating an Application in Flask</h2>
Flask is a micro web framework written in Python. To create the Doctor FOOD application, we used Flask to define the endpoints and handle the HTTP requests.
<h2>Local Deployment - Using Bash Script</h2>
To deploy the Doctor FOOD application locally, we can use a bash script. The script will install the necessary dependencies, run the Flask application, and set the required environment variables.
<h2>Build a Docker Image</h2>
To containerize the Doctor FOOD application, we can build a Docker image using the Dockerfile provided in the application's repository. The Dockerfile will specify the application's dependencies and expose the required ports.
<h2>Push Image into a Container Registry</h2>
To push the Docker image to a container registry, we can use a command-line interface such as Docker CLI or Azure CLI. This will allow us to store and manage the Docker image for later use.
<h2>Push Image into an Azure Container Registry</h2>
To deploy the Doctor FOOD application on the cloud, we can use an Azure Container Registry. This will allow us to store and manage the Docker image in a secure and scalable way.
<h2>Deploy the Image Using Docker</h2>
To deploy the Doctor FOOD application using Docker, we can use a command-line interface such as Docker CLI or Azure CLI. This will allow us to run the Docker image as a container and expose the required ports.
<h2>Deploy the Image Using Kubernetes</h2>
To deploy the Doctor FOOD application using Kubernetes, we can use Kubernetes CLI or Azure Kubernetes Service (AKS). This will allow us to create a Kubernetes cluster and deploy the application as a Kubernetes deployment.
<h2>Test Liveness Endpoint Using Curl Request</h2>
To test the liveness endpoint of the Doctor FOOD application, we can use a curl request. This will allow us to check if the application is running and responding to requests.
<h2>Cloud Deployment - Using Pipelines</h2>
To deploy the Doctor FOOD application on the cloud using Azure pipelines, we can use Azure DevOps. This will allow us to create a pipeline that automates the deployment process and integrates with our source code repository.
<h2>Azure WebApp Container</h2>
To deploy the Doctor FOOD application on Azure WebApp Container, we can use Azure CLI or Azure portal. This will allow us to create a WebApp Container and deploy the Docker image on it.
<h2>Azure CLI</h2>
Azure CLI este o interfață de linie de comandă care ne permite să interacționăm cu serviciile Azure. Putem folosi Azure CLI pentru a gestiona și a automatiza diferite operațiuni în cadrul soluțiilor noastre Azure, inclusiv în ceea ce privește Doctor FOOD.
<h2>Kubernetes</h2>
Kubernetes este un sistem open-source de automatizare a deploimentelor, scalare și gestionare a aplicațiilor containerizate. Putem utiliza Kubernetes pentru a gestiona și a scala aplicația Doctor FOOD în mod eficient în cadrul unui mediu de cloud. Kubernetes CLI sau servicii precum Azure Kubernetes Service (AKS) ne permit să rulăm și să gestionăm cluster-e Kubernetes, iar astfel putem folosi acestea pentru a rula și a gestiona aplicația Doctor FOODs

<h2>/foods</h2>
The /foods endpoint allows users to view all the foods stored in the application's database.
<h2>/lowCalories</h2>
The /lowCalories endpoint allows users to view all the low calorie foods stored in the application's database.
<h2>/addFood</h2>
The /addFood endpoint allows users to add new foods to the application's database.
<h2>/deleteFood</h2>
The /deleteFood endpoint allows users to delete existing foods from the application's database.
<h2>/api</h2>
The /api endpoint allows users to access the application's API documentation.
<h2>/apiOrdonat</h2>
The /apiOrdonat endpoint allows users to view all the foods stored in the application's database sorted in alphabetical order.
<h2>/liveness</h2>
The /liveness endpoint allows users to test if the application is running and responding to requests.
<h2>/check_api</h2>
The /check_api endpoint allows users to check the status of the application's API.
<h2>/prezentare</h2>
The /prezentare endpoint provides a brief introduction to the Doctor FOOD application.
<h2>/contact</h2>
The /contact endpoint provides contact information for the developers of the Doctor FOOD application.