import json
from pathlib import Path

PORTFOLIO_FILE = Path('portfolio.json')

class PortfolioManager:
    """Manage stock holdings stored in a JSON file."""

    def __init__(self, path: Path = PORTFOLIO_FILE):
        self.path = path
        if not self.path.exists():
            self._write({})

    def _read(self) -> dict:
        with self.path.open('r') as f:
            return json.load(f)

    def _write(self, data: dict) -> None:
        with self.path.open('w') as f:
            json.dump(data, f, indent=2)

    def add(self, symbol: str):
        data = self._read()
        data[symbol.upper()] = {}
        self._write(data)

    def remove(self, symbol: str):
        data = self._read()
        data.pop(symbol.upper(), None)
        self._write(data)

    def list(self):
        return list(self._read().keys())
