import argparse
from .portfolio import PortfolioManager
from .market import MarketAPI
from .report import DailyReporter


def main(argv=None):
    parser = argparse.ArgumentParser(description="Stock portfolio CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_p = subparsers.add_parser("add", help="Add a stock to portfolio")
    add_p.add_argument("symbol")

    rm_p = subparsers.add_parser("remove", help="Remove a stock from portfolio")
    rm_p.add_argument("symbol")

    subparsers.add_parser("list", help="List portfolio")
    subparsers.add_parser("report", help="Generate daily report")

    args = parser.parse_args(argv)
    pm = PortfolioManager()
    market = MarketAPI()

    if args.command == "add":
        pm.add(args.symbol)
    elif args.command == "remove":
        pm.remove(args.symbol)
    elif args.command == "list":
        for s in pm.list():
            print(s)
    elif args.command == "report":
        reporter = DailyReporter(pm, market)
        print(reporter.generate())
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
