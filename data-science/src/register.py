
import os
import argparse
import logging
import mlflow
import pandas as pd
from pathlib import Path

#mlflow.start_run()  # Starting the MLflow experiment run

def parse_args():
    '''Parse input arguments'''

    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', type=str, help='Name under which model will be registered')  # Hint: Specify the type for model_name (str)
    parser.add_argument('--model_path', type=str, help='Model directory')  # Hint: Specify the type for model_path (str)
    parser.add_argument("--model_info_output_path", type=str, help="Path to write model info JSON")  # Hint: Specify the type for model_info_output_path (str)
    args, _ = parser.parse_known_args()
    print(f'Arguments: {args}')

    return args

def main(args):
    # Argument parser setup for command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, help="Path to the trained model")  # Path to the trained model artifact
    args = parser.parse_args()

    # Load the trained model from the provided path
    model = mlflow.sklearn.load_model(Path(args.model))  # _______ (Fill the code to load model from args.model)

    print("Registering the best trained used cars price prediction model")
    
    # Register the model in the MLflow Model Registry under the name "price_prediction_model"
    mlflow.sklearn.log_model(
        sk_model=model,
        registered_model_name="car_prediction_model",  # Specify the name under which the model will be registered
        artifact_path="random_forest_price_classifier"  # Specify the path where the model artifacts will be stored
    )

    # End the MLflow run
    mlflow.end_run()  # ________ (Fill in the code to end the MLflow run)

if __name__ == "__main__":

    mlflow.start_run()
    
    # Parse Arguments
    args = parse_args()
    
    lines = [
        f"Model name: {args.________}",
        f"Model path: {args.________}",
        f"Model info output path: {args.________}"
    ]

    for line in lines:
        print(line)

    main(args)

    mlflow.end_run()
