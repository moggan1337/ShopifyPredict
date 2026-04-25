# ShopifyPredict

<p align="center">
  <img src="https://img.shields.io/badge/Shopify-ML%20Integration-95BF47?style=for-the-badge&logo=shopify&logoColor=white" alt="Shopify">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

> 📈 **ML-Powered Demand Forecasting** - Predict inventory needs, optimize stock levels, reduce overstock by 40% using Prophet and LSTM models integrated with Shopify.

## ✨ Features

### Demand Forecasting
- 📊 **Time Series Prediction** - Prophet-based daily/weekly/monthly forecasts
- 🧠 **Deep Learning** - LSTM models for complex seasonal patterns
- 🎯 **Product-Level** - Individual forecasts per SKU
- 📦 **Category-Level** - Aggregate forecasts for categories
- 🌐 **Multi-Store** - Cross-store predictions for franchises

### Inventory Optimization
- 📈 **Reorder Points** - Calculate optimal reorder triggers
- 💰 **Safety Stock** - Dynamic safety stock calculations
- ⚡ **Lead Time** - Adjust for supplier lead times
- 🔄 **Auto-Replenishment** - Trigger purchase orders automatically
- 📉 **Dead Stock** - Identify slow-moving inventory

### Analytics Dashboard
- 📊 **Forecast Accuracy** - Track prediction vs actual
- 📉 **Trends** - Product trend analysis
- 🔮 **What-If** - Scenario planning
- 📱 **Mobile App** - iOS/Android dashboards
- 📧 **Alerts** - Email/Slack notifications

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      ShopifyPredict System                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    Data Ingestion Layer                    │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐ │   │
│  │  │ Shopify  │ │  POS     │ │  Excel   │ │  ERP Systems  │ │   │
│  │  │   API     │ │  Data    │ │  Import  │ │  (SAP, Oracle)│ │   │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────────┘ │   │
│  └──────────────────────────────────────────────────────────┘   │
│                             │                                    │
│  ┌──────────────────────────┴──────────────────────────────────┐ │
│  │                    Feature Engineering                        │ │
│  │  - Historical Sales Features                                  │ │
│  │  - Calendar Features (holidays, events)                       │ │
│  │  - Price Elasticity                                           │ │
│  │  - External Factors (weather, trends)                        │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                             │                                    │
│  ┌──────────────────────────┴──────────────────────────────────┐ │
│  │                    ML Model Layer                             │ │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐ │ │
│  │  │   Prophet  │ │    LSTM    │ │  Ensemble  │ │  XGBoost   │ │ │
│  │  │  (Trend +  │ │ (Deep     │ │  (Combine  │ │ (Feature   │ │ │
│  │  │  Seasonal) │ │  Learning)│ │  Models)  │ │  Importance)│ │ │
│  │  └────────────┘ └────────────┘ └────────────┘ └────────────┘ │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                             │                                    │
│  ┌──────────────────────────┴──────────────────────────────────┐ │
│  │                    Prediction Service                        │ │
│  │  - Daily Forecasts (30/60/90 days)                          │ │
│  │  - Reorder Point Calculation                                │ │
│  │  - Safety Stock Levels                                      │ │
│  │  - Stockout Risk Assessment                                 │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                             │                                    │
│  ┌──────────────────────────┴──────────────────────────────────┐ │
│  │                    Output Layer                              │ │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐ │ │
│  │  │ Dashboard │ │   API    │ │ Webhooks │ │  Shopify Sync    │ │ │
│  │  │  (React)  │ │  (FastAPI)│ │ (Alerts) │ │  (Inventory)    │ │ │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────────────┘ │ │
│  └──────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/moggan1337/ShopifyPredict.git
cd ShopifyPredict

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install ML packages
pip install -r requirements-ml.txt

# Copy environment variables
cp .env.example .env

# Configure .env with your credentials
```

## 🚀 Quick Start

```bash
# 1. Start the API server
uvicorn api.main:app --reload

# 2. Start the dashboard
cd dashboard && npm install && npm run dev

# 3. Connect your Shopify store in settings

# 4. Trigger initial forecast
curl -X POST http://localhost:8000/api/forecast/run

# 5. View predictions in dashboard
# http://localhost:3000
```

## 📊 API Reference

### Forecasts

```bash
# Get forecast for a product
GET /api/forecast/{product_id}

# Response
{
  "product_id": "gid://shopify/Product/123",
  "forecast": {
    "2024-11-01": { "predicted": 45, "lower": 38, "upper": 52 },
    "2024-11-02": { "predicted": 48, "lower": 41, "upper": 55 },
    ...
  },
  "accuracy": 0.94,
  "model": "prophet_ensemble"
}
```

### Reorder Recommendations

```bash
# Get reorder recommendations
GET /api/reorder/recommendations

# Response
{
  "recommendations": [
    {
      "product_id": "gid://shopify/Product/123",
      "sku": "WIDGET-001",
      "current_stock": 15,
      "reorder_point": 25,
      "reorder_quantity": 100,
      "days_until_stockout": 5,
      "urgency": "high"
    },
    ...
  ]
}
```

## 🔧 Configuration

```env
# Shopify
SHOPIFY_STORE_DOMAIN=your-store.myshopify.com
SHOPIFY_ACCESS_TOKEN=shpat_xxxxx

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/shopifypredict
REDIS_URL=redis://localhost:6379

# ML Settings
FORECAST_HORIZON_DAYS=90
CONFIDENCE_INTERVAL=0.95
AUTO_RETRAIN_DAYS=7

# Alerts
SLACK_WEBHOOK_URL=https://hooks.slack.com/...
ALERT_EMAIL=alerts@example.com
```

## 📁 Project Structure

```
shopify-predict/
├── api/
│   ├── main.py              # FastAPI app
│   ├── routes/
│   │   ├── forecast.py      # Forecast endpoints
│   │   ├── inventory.py     # Inventory endpoints
│   │   └── alerts.py        # Alert endpoints
│   └── services/
│       ├── ml_service.py     # ML model inference
│       └── shopify_service.py
├── ml/
│   ├── models/
│   │   ├── prophet_model.py
│   │   ├── lstm_model.py
│   │   └── ensemble.py
│   ├── features/
│   │   ├── sales_features.py
│   │   └── calendar_features.py
│   └── training/
│       ├── train.py
│       └── evaluate.py
├── dashboard/
│   ├── app/                 # Next.js dashboard
│   └── components/
└── notebooks/
    └── analysis.ipynb       # EDA notebooks
```

## 🧠 ML Models

### Prophet (Trend + Seasonality)

```python
from prophet import Prophet

model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False,
    seasonality_mode='multiplicative'
)

model.fit(df_sales)
forecast = model.predict(df_future)
```

### LSTM (Deep Learning)

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

model = Sequential([
    LSTM(64, return_sequences=True, input_shape=(timesteps, features)),
    LSTM(32),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=100, batch_size=32)
```

### Ensemble (Combined)

```python
# Weighted average of predictions
final_prediction = (
    0.4 * prophet_pred +
    0.4 * lstm_pred +
    0.2 * xgboost_pred
)
```

## 📈 Dashboard Screenshots

| Dashboard | Features |
|-----------|----------|
| **Overview** | Total SKUs, stockout alerts, forecast accuracy |
| **Forecasts** | Interactive charts, confidence intervals |
| **Inventory** | Current stock, reorder points, safety stock |
| **Trends** | Top movers, seasonal patterns |
| **Alerts** | Slack/email notifications |

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=ml --cov=api --cov=dashboard

# Test specific model
pytest tests/ml/test_prophet.py -v

# Run integration tests
pytest tests/integration/ -v
```

## 📚 Documentation

- [Installation Guide](docs/installation.md)
- [API Reference](docs/api.md)
- [ML Models](docs/ml-models.md)
- [Dashboard Guide](docs/dashboard.md)
- [Deployment](docs/deployment.md)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Run tests
4. Submit PR

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

<p align="center">
  Predict the future, optimize the present
</p>
