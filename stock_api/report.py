from datetime import datetime
from .portfolio import PortfolioManager
from .market import MarketAPI

class DailyReporter:
    """Generate daily report for portfolio holdings."""

    def __init__(self, portfolio: PortfolioManager, market: MarketAPI):
        self.portfolio = portfolio
        self.market = market

    def generate(self) -> str:
        report_lines = [f"Daily Report - {datetime.utcnow().date()}\n"]
        for symbol in self.portfolio.list():
            quote = self.market.price_quote(symbol)
            news = self.market.company_news(symbol)
            price = quote.get('05. price', 'N/A')
            volume = quote.get('06. volume', 'N/A')
            report_lines.append(f"{symbol}: price={price}, volume={volume}")
            if news:
                report_lines.append(f"News for {symbol}:")
                for article in news[:3]:
                    title = article.get('title')
                    url = article.get('url')
                    report_lines.append(f" - {title} ({url})")
            report_lines.append('')
        return "\n".join(report_lines)
