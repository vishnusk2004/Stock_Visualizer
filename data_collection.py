import requests
import pandas as pd

API_KEY = '9RKDHJB5H7N4MZQ8'  # Replace with your Alpha Vantage API key

def get_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

def main():
    # Example stock symbols
    symbols = ['AAPL', 'MSFT', 'GOOGL']
    all_data = []

    for symbol in symbols:
        data = get_stock_data(symbol)
        all_data.append(data)

    df = pd.DataFrame(all_data)
    df.to_csv('stock_data.csv', index=False)
    print("Data saved to stock_data.csv")

if __name__ == '__main__':
    main()
