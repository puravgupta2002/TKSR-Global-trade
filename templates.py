import os 
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

project_name="datascience_project"
file_name=[
    "main.py",
    "Terraform/main.tf",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
]

for filepath in file_name:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory {filedir} for the file : {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filename)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} is already existed ")