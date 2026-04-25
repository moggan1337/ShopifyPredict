# ShopifyPredict - Development Guide

## Project Overview

**ShopifyPredict** is an ML-based demand forecasting system for Shopify stores. It uses Prophet and LSTM models to predict future product demand based on historical sales data.

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Runtime** | Python 3.10+ |
| **ML Models** | Prophet, TensorFlow/Keras |
| **Data** | Pandas, NumPy |
| **Visualization** | Matplotlib |
| **API** | Shopify Admin API |

## Project Structure

```
ShopifyPredict/
├── src/
│   ├── __init__.py
│   ├── cli.py              # CLI entry point
│   ├── forecaster.py       # Main forecasting logic
│   ├── fetcher.py          # Shopify data fetcher
│   └── visualizer.py       # Plotting
├── requirements.txt
├── setup.py
├── CLAUDE.md
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python -m shopify_predict --store mystore.myshopify.com --token shpat_xxx --product-id xyz --days 30
```

## Models

### Prophet
Facebook's Prophet model for time series forecasting with seasonality.

### LSTM
Long Short-Term Memory neural network for sequence prediction.

## LLM Integration

Uses MiniMax API for:
- Demand trend analysis
- Anomaly detection suggestions
- Natural language forecast summaries
