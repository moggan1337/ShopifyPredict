#!/usr/bin/env python3
"""
ShopifyPredict CLI - Demand Forecasting for Shopify Stores
"""

import argparse
import sys
from .forecaster import ShopifyForecaster

def main():
    parser = argparse.ArgumentParser(description='ShopifyPredict - ML Demand Forecasting')
    parser.add_argument('--store', required=True, help='Shopify store domain')
    parser.add_argument('--token', required=True, help='Shopify access token')
    parser.add_argument('--product-id', help='Specific product ID to forecast')
    parser.add_argument('--days', type=int, default=30, help='Forecast horizon in days')
    parser.add_argument('--model', choices=['prophet', 'lstm', 'auto'], default='auto',
                        help='Forecasting model to use')
    parser.add_argument('--output', help='Output file for forecasts')
    
    args = parser.parse_args()
    
    forecaster = ShopifyForecaster(args.store, args.token)
    
    if args.product_id:
        forecast = forecaster.forecast_product(args.product_id, args.days, args.model)
        print(f"Forecast for product {args.product_id}:")
        print(forecast)
    else:
        forecast = forecaster.forecast_all(args.days, args.model)
        print(f"Forecasts for {len(forecast)} products:")
        for product_id, data in forecast.items():
            print(f"  {product_id}: {data}")

if __name__ == '__main__':
    main()
