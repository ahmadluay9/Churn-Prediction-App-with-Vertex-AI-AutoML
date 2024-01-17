# Churn-Prediction-App-with-Vertex-AI-AutoML

- [Previous Project]('https://github.com/ahmadluay9/Customer-Churn-Prediction')
  
- [Application Demo]()

"Churn Prediction App with Vertex AI AutoML" is a project that leverages the capabilities of Vertex AI AutoML to develop an intelligent application focused on predicting and mitigating customer churn. By predicting customer churn, a company can take proactive measures to retain these customer.

---

## File Explanation
This repository consists of several files :
```
    ├── backend/
    │   ├── app.py
    │   ├── ctelkom-dbe404744ae4.json
    │   ├── Dockerfile
    │   ├── requirements.txt
    ├── frontend/
    │   ├── app.py
    │   ├── Dockerfile
    │   ├── requirements.txt
    ├── docker-compose
    ├── README.md
    ├── requirements.txt
    ├── sample_10.csv
    └── Vertex_AI_Notebook.ipynb
```

- `backend/ app.py`: This file  contains the backend code for the application. It responsible for handling server-side logic, API endpoints, or any other backend functionality.

- `backend/ ctelkom-dbe404744ae4.json`: This is a service account JSON key file. It is used for authenticating application to Google Cloud services.

- `backend/ Dockerfile`: Dockerfile is used to build a Docker image for backend application. It includes instructions on how to set up the environment and dependencies needed for backend.

- `backend/ requirements.txt`: This file lists the Python dependencies required for backend application. These dependencies can be installed using a package manager like pip.

- `frontend/ app.py`: This file is the main script for the frontend of the application and is developed using the Streamlit framework. It contain sections for user input, and the integration of backend functionality through API calls. 

- `frontend/ Dockerfile`: Similar to the backend Dockerfile, this file is used to build a Docker image for frontend application. It includes instructions on setting up the environment and installing dependencies.

- `frontend/ requirements.txt`: This file lists the Python dependencies required for frontend application. These dependencies can be installed using a package manager like pip. 

- `docker-compose` : This is a configuration file for Docker Compose. It defines services, networks, and volumes for your application's containers. Docker Compose simplifies the process of running multi-container applications.

- `README.md`: This is a Markdown file that typically contains documentation for the project. It include information on how to set up and run your application, dependencies, and any other relevant details.

- `sample_10.csv`: This is a CSV file that contains sample data for testing. It used as input data for the application.

- `Vertex_AI_Notebook.ipynb`: This Jupyter Notebook file contain code, analysis, or documentation related to machine learning tasks using Google Cloud's Vertex AI.

---

## Model

The model used is a model trained using **Vertex AI AutoML**. Vertex AI provides a comprehensive and user-friendly platform for developing, deploying, and managing machine learning models, enabling you to focus on solving business problems rather than managing infrastructure and complexities.

### Model Evaluation
![Alt text](image-2.png)
![Alt text](image-3.png)


The model evaluation metrics indicate excellent performance:

- `PR AUC` (Precision-Recall Area Under the Curve): 0.98 - High precision and recall across different thresholds.
- `ROC AUC` (Receiver Operating Characteristic Area Under the Curve): 0.98 - Strong discrimination between positive and negative classes.
- `Log Loss`: 0.164 - Predicted probabilities closely match actual class labels.
- `F1 Score`: 0.93 - Good balance between precision and recall.
- `Micro-F1`: 0.93 - Overall strong performance across all classes.
- `Macro-F1`: 0.93 - High average F1 score across different classes.
- `Precision`: 92.6% - Accurate identification of positive instances.
- `Recall`: 92.6% - Capturing a high percentage of actual positive instances.

![Alt text](image-4.png)

- `True Positive (TP)`: 93% - The model correctly predicted instances as "churn" (label 1) when the true label was indeed "churn."

- `False Negative (FN)`: 7% - The model incorrectly predicted instances as "not churn" (label 0) when the true label was "churn."

- `False Positive (FP)`: 8% - The model incorrectly predicted instances as "churn" (label 1) when the true label was "not churn."

- `True Negative (TN)`: 92% - The model correctly predicted instances as "not churn" (label 0) when the true label was indeed "not churn."

High sensitivity and specificity, along with precision, indicate a model that is effective in identifying both churn and non-churn instances. However, it's worth noting that the false positive rate is 8%, indicating that there is some misclassification of "not churn" instances as "churn." Depending on the specific requirements and costs associated with false positives, further optimization may be considered.

---

## Application
### Architecture
![streamlit with fastapi](image.png)

### Project Setup

- Clone this repository

```shell
(base)$: git clone https://github.com/ahmadluay9/Churn-Prediction-App-with-Vertex-AI-AutoML.git
(base)$: cd Churn-Prediction-App-with-Vertex-AI-AutoML
```

- Run the applications

```shell
$ docker-compose build
$ docker-compose up
```

- To visit the FastAPI documentation of the resulting service, visit [http://localhost:8000/docs](http://localhost:8000/docs) with a web browser. To visit the streamlit UI, visit [http://localhost:8501](http://localhost:8501).

---

## Results

---

## Conclusions 

The "Churn Prediction App with Vertex AI AutoML" successfully taps into the potential of Vertex AI AutoML, offering an intelligent solution for predicting and addressing customer churn. The model, trained using Vertex AI AutoML, exhibits commendable performance across various evaluation metrics, showcasing its ability to accurately identify both churn and non-churn instances. The balanced F1 score, high precision and recall, and discrimination power reflected in ROC AUC and PR AUC underscore the model's effectiveness.

The application's architecture, with FastAPI on the backend and Streamlit on the frontend, provides a seamless and user-friendly experience. However, it's crucial to consider the 8% false positive rate, indicating instances where "not churn" is misclassified as "churn." Depending on specific business requirements and the associated costs of false positives, further fine-tuning and optimization may be explored.














