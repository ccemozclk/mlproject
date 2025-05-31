import sys
import os

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

from src.exception import CustomException
from src.logger import logging

def run_training_pipeline():
    try:
        logging.info("Starting the end-to-end training pipeline...")

        # 1. Data Ingestion
        ingestion = DataIngestion()
        train_data_path, test_data_path = ingestion.initiate_data_ingestion()
        logging.info(f"Data Ingestion completed. Train: {train_data_path}, Test: {test_data_path}")

        # 2. Data Transformation
        transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = transformation.initiate_data_transformation(
            train_data_path, test_data_path
        )
        logging.info(f"Data Transformation completed. Preprocessor saved at: {preprocessor_path}")

        # 3. Model Training
        trainer = ModelTrainer()
        r2_score = trainer.initiate_model_trainer(train_arr, test_arr)
        logging.info(f"Model Training completed. R2 Score: {r2_score}")

        print(f"\n🎉 Training pipeline completed successfully! R2 Score: {r2_score:.4f}")

    except CustomException as ce:
        logging.error(f"CustomException occurred: {str(ce)}")
        raise ce

    except Exception as e:
        logging.error(f"Unexpected error in training pipeline: {str(e)}")
        raise CustomException(e, sys)


if __name__ == "__main__":
    run_training_pipeline()