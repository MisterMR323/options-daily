import argparse

def generate_report(watchlist):
    # Add your logic here to fetch data and generate reports
    print(f"Generating report for: {', '.join(watchlist)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--guidance",
        nargs="+",
        help="List of stock tickers to include in the report",
    )
    args = parser.parse_args()
    generate_report(args.guidance)
