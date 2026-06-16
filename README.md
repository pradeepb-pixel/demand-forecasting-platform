<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a192f,50:112240,100:2D7EFF&height=180&section=header&text=Demand%20Forecasting%20Platform&fontSize=32&fontColor=64ffda&fontAlignY=45&desc=GCP%20Vertex%20AI%20%7C%20BigQuery%20%7C%20Python%20%7C%20Spark&descSize=15&descAlignY=68&descColor=8892b0&animation=fadeIn" width="100%"/>

</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-64ffda?style=flat-square&logo=python&logoColor=0a192f)
![Vertex AI](https://img.shields.io/badge/GCP-Vertex_AI-4285F4?style=flat-square&logo=google-cloud&logoColor=white)
![BigQuery](https://img.shields.io/badge/GCP-BigQuery-4285F4?style=flat-square&logo=google-bigquery&logoColor=white)
![Spark](https://img.shields.io/badge/Apache-Spark-E25A1C?style=flat-square&logo=apache-spark&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Enabled-64ffda?style=flat-square&logo=pandas&logoColor=0a192f)
![Status](https://img.shields.io/badge/Status-Production-success?style=flat-square)

</div>

---

## 🧠 Overview

A **production-grade predictive demand forecasting platform** built on **GCP Vertex AI** — designed to optimize inventory planning, reduce stock shortages, and deliver measurable cost savings across healthcare supply chains.

Deployed at **CVS Health** to forecast product demand across multiple distribution centers using historical transaction data and ML models trained on GCP.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                       DATA INGESTION LAYER                          │
│           Historical Sales  ·  Inventory  ·  External Signals       │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     DATA PROCESSING LAYER                           │
│              BigQuery  ·  Dataflow  ·  Apache Spark                 │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      ML TRAINING LAYER                              │
│                    GCP Vertex AI Training                           │
│         Time Series Models  ·  Feature Engineering  ·  AutoML      │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     PREDICTION LAYER                                │
│              Vertex AI Endpoints  ·  Batch Predictions              │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    VISUALIZATION LAYER                              │
│              Looker  ·  Power BI  ·  BigQuery Dashboards           │
└─────────────────────────────────────────────────────────────────────┘
```

---

## ⚡ Key Features

| Feature | Description |
|---|---|
| 📈 **Time Series Forecasting** | Multi-horizon demand predictions (daily, weekly, monthly) |
| 🧠 **Vertex AI Training** | Scalable ML model training on GCP infrastructure |
| 🔄 **Automated Retraining** | Models retrain automatically on new data |
| 📊 **BigQuery Integration** | Petabyte-scale data processing for feature engineering |
| ⚡ **Batch Predictions** | High-volume forecasting across thousands of SKUs |
| 📉 **Shortage Reduction** | Proactive alerts when stock levels fall below forecasted demand |
| 📋 **Dashboard Reporting** | Real-time inventory insights via Looker and Power BI |
| 🔁 **Pipeline Automation** | End-to-end automated data → forecast → report pipeline |

---

## 🛠️ Tech Stack

```python
tech_stack = {
    "ml_platform"    : ["GCP Vertex AI", "AutoML", "Custom Training"],
    "data_warehouse" : ["BigQuery", "Dataflow", "Pub/Sub"],
    "processing"     : ["Apache Spark", "Pandas", "NumPy"],
    "language"       : ["Python 3.10+", "SQL"],
    "visualization"  : ["Looker", "Power BI", "BigQuery BI Engine"],
    "storage"        : ["GCS (Google Cloud Storage)", "BigQuery"],
    "monitoring"     : ["Vertex AI Model Monitoring", "Cloud Logging"],
}
```

---

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.10+
GCP Account with Vertex AI + BigQuery access
Google Cloud SDK configured
```

### Installation

```bash
# Clone the repo
git clone https://github.com/pradeepb-pixel/demand-forecasting-platform.git
cd demand-forecasting-platform

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

```bash
# Set your GCP credentials
export GOOGLE_APPLICATION_CREDENTIALS=path/to/service_account.json
export GCP_PROJECT_ID=your_project_id
export GCP_REGION=us-central1

# Set BigQuery dataset
export BQ_DATASET=demand_forecasting
```

### Run

```bash
# Run data pipeline
python pipeline/data_pipeline.py

# Train forecasting model
python training/train.py

# Generate predictions
python prediction/predict.py
```

---

## 📁 Project Structure

```
demand-forecasting-platform/
│
├── pipeline/
│   ├── data_pipeline.py       # Data ingestion & preprocessing
│   ├── feature_engineering.py # Feature creation from raw data
│   └── dataflow_job.py        # GCP Dataflow pipeline
│
├── training/
│   ├── train.py               # Vertex AI training job launcher
│   ├── model.py               # Forecasting model definition
│   └── evaluate.py            # Model evaluation & metrics
│
├── prediction/
│   ├── predict.py             # Batch prediction runner
│   ├── vertex_endpoint.py     # Vertex AI endpoint client
│   └── alert_generator.py     # Low stock alert system
│
├── visualization/
│   └── dashboard_config.py    # Looker / Power BI config
│
├── config/
│   └── settings.py            # Configuration & environment vars
│
├── pipeline/data_pipeline.py  # Entry point
├── requirements.txt
└── README.md
```

---

## 🔄 How It Works

**1. Data Ingestion** — Historical sales, inventory, and external signals pulled into BigQuery

**2. Feature Engineering** — Spark + Dataflow transforms raw data into ML-ready features

**3. Model Training** — Vertex AI trains time series forecasting models at scale

**4. Predictions Generated** — Batch predictions across all SKUs and locations

**5. Alerts Triggered** — Automatic low-stock alerts when forecast signals shortage risk

**6. Dashboard Updated** — Inventory teams see real-time forecasts in Looker / Power BI

---

## 📊 Results

| Metric | Outcome |
|---|---|
| 📈 Forecast Accuracy | High accuracy across multi-horizon predictions |
| 📉 Stock Shortages | Significant reduction in out-of-stock incidents |
| ⚡ Processing Speed | Large-scale SKU forecasting with Spark + BigQuery |
| 💰 Cost Savings | Reduced overstock and emergency procurement costs |
| 🔄 Pipeline Automation | Fully automated end-to-end forecast pipeline |

---

## 🏢 Built At

Designed and deployed as part of Data Science work at **CVS Health** — optimizing inventory planning across healthcare supply chains with production-grade ML on GCP.

---

## 👤 Author

**Pradeep B** — AI Engineer | Data Scientist

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0a192f?style=flat-square&logo=linkedin&logoColor=64ffda)](https://linkedin.com/in/1199pb123)
[![Email](https://img.shields.io/badge/Email-0a192f?style=flat-square&logo=gmail&logoColor=64ffda)](mailto:pradeepb4646@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-0a192f?style=flat-square&logo=vercel&logoColor=64ffda)](https://pradeepb.dev)

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2D7EFF,50:112240,100:0a192f&height=100&section=footer" width="100%"/>

</div>
