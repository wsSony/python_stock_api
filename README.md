# Python Stock API

This repository provides a small command line tool for tracking a simple stock portfolio.

## Features

- Add or remove holdings which are stored locally in `portfolio.json`.
- Fetch current stock quotes and recent news using the Alpha Vantage and NewsAPI services.
- Generate a daily report summarising prices and news for all holdings.

## Usage

Set the environment variables `ALPHAVANTAGE_API_KEY` and `NEWSAPI_KEY` with your API keys.

```bash
python -m stock_api add AAPL
python -m stock_api report
```

## Disclaimer

Network requests are required to fetch prices and news. Ensure that outbound internet
access is enabled and that you supply valid API keys.
