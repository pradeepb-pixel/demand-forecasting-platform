import os
from dotenv import load_dotenv
load_dotenv()

GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID", "")
GCP_REGION = os.getenv("GCP_REGION", "us-central1")
BQ_DATASET = os.getenv("BQ_DATASET", "demand_forecasting")
VERTEX_BUCKET = os.getenv("VERTEX_BUCKET", "gs://your-bucket")
