import os
from datetime import datetime
from typing import Optional
import requests

ALPHAVANTAGE_URL = 'https://www.alphavantage.co/query'
NEWS_URL = 'https://newsapi.org/v2/everything'

class MarketAPI:
    """Fetch stock price and news information using external APIs."""

    def __init__(self, alpha_key: Optional[str] = None, news_key: Optional[str] = None):
        self.alpha_key = alpha_key or os.getenv('ALPHAVANTAGE_API_KEY')
        self.news_key = news_key or os.getenv('NEWSAPI_KEY')

    def price_quote(self, symbol: str) -> dict:
        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': symbol,
            'apikey': self.alpha_key,
        }
        response = requests.get(ALPHAVANTAGE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json().get('Global Quote', {})

    def company_news(self, symbol: str) -> list:
        if not self.news_key:
            return []
        today = datetime.utcnow().date()
        yesterday = today.fromordinal(today.toordinal() - 1)
        params = {
            'q': symbol,
            'from': yesterday.isoformat(),
            'to': today.isoformat(),
            'sortBy': 'publishedAt',
            'apiKey': self.news_key,
            'language': 'en',
        }
        response = requests.get(NEWS_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get('articles', [])
