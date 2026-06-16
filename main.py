"""
Demand Forecasting Platform
Built on GCP Vertex AI for CVS Health Supply Chain
Author: Pradeep B | Data Scientist @ CVS Health
"""

from pipeline.data_pipeline import DataPipeline
from training.train import ForecastingModel
from prediction.predict import PredictionEngine

def run_forecasting_pipeline():
    """
    End-to-end demand forecasting pipeline:
    Data → Features → Train → Predict → Alert
    """
    print("Step 1: Running data pipeline...")
    pipeline = DataPipeline()
    data = pipeline.run()

    print("Step 2: Training forecasting model on Vertex AI...")
    model = ForecastingModel()
    model.train(data)

    print("Step 3: Generating demand predictions...")
    predictor = PredictionEngine()
    predictions = predictor.predict(data)

    print(f"Forecasting complete. {len(predictions)} SKUs predicted.")
    return predictions


if __name__ == "__main__":
    run_forecasting_pipeline()
