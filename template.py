import os
from pathlib import Path

project_name = "src"

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",
    f"{project_name}/configuration/aws_connection.py",
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_storage.py",
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/proj1_data.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",
    f"{project_name}/entity/s3_estimator.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")



# MLOPS-PROJECT/
# ├── src/                            # Source code for the project
# │   ├── __init__.py                 # Marks src as a Python package
# │   ├── components/                 # ML pipeline components
# │   │   ├── __init__.py
# │   │   ├── data_ingestion.py       # Data ingestion logic
# │   │   ├── data_validation.py      # Data validation logic
# │   │   ├── data_transformation.py  # Data preprocessing logic
# │   │   ├── model_training.py       # Model training logic
# │   │   ├── model_evaluation.py     # Model evaluation logic
# │   │   ├── model_pusher.py         # Deployment logic
# │   ├── pipelines/                  # End-to-end pipelines
# │   │   ├── __init__.py
# │   │   ├── training_pipeline.py    # Training pipeline
# │   │   ├── prediction_pipeline.py  # Prediction pipeline
# │   ├── utils/                      # Utility functions
# │   │   ├── __init__.py
# │   │   ├── file_operations.py      # File handling utilities
# │   │   ├── logger.py               # Custom logger
# │   │   ├── metrics.py              # Evaluation metrics
# │   ├── config/                     # Configuration files and constants
# │   │   ├── __init__.py
# │   │   ├── config.py               # Global config handling
# │   │   ├── schema.yaml             # Data schema definition
# │   │   ├── model.yaml              # Model-specific configurations
# │   ├── exception/                  # Custom exceptions
# │   │   ├── __init__.py
# │   │   ├── custom_exceptions.py    # Exception handling
# │   ├── data_access/                # Data access logic
# │   │   ├── __init__.py
# │   │   ├── database_operations.py  # Interact with databases
# │   │   ├── cloud_storage.py        # Interact with cloud storage
# │   ├── entity/                     # Entities for configurations and artifacts
# │   │   ├── __init__.py
# │   │   ├── config_entity.py        # Configuration dataclasses
# │   │   ├── artifact_entity.py      # Artifacts produced by pipeline steps
# │   ├── tests/                      # Unit and integration tests
# │       ├── __init__.py
# │       ├── test_data_ingestion.py
# │       ├── test_model_training.py
# ├── notebooks/                      # Jupyter notebooks for prototyping
# │   ├── exploration.ipynb           # Data exploration notebook
# │   ├── model_testing.ipynb         # Model testing notebook
# ├── artifacts/                      # Outputs of pipelines
# │   ├── data/                       # Processed and intermediate data
# │   ├── models/                     # Saved models
# │   ├── logs/                       # Logs from pipeline runs
# ├── config/                         # Project configuration files
# │   ├── .env                        # Environment variables
# ├── scripts/                        # Standalone scripts
# │   ├── data_upload.py              # Script to upload data
# │   ├── trigger_training.py         # Script to trigger training
# ├── Dockerfile                      # Docker image definition
# ├── .dockerignore                   # Files to ignore during Docker build
# ├── requirements.txt                # Python dependencies
# ├── pyproject.toml                  # Modern build system configuration
# ├── setup.py                        # Legacy build configuration
# ├── README.md                       # Project documentation
# ├── LICENSE                         # License file
# ├── .gitignore                      # Files to ignore in Git
# ├── .github/                        # GitHub-specific configurations
# │   ├── workflows/                  # CI/CD workflows
# │       ├── mlops-pipeline.yml      # Workflow for CI/CD pipelines
