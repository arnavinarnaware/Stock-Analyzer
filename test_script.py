from stock_analysis import get_stock_prices, insert_data_into_mysql

api_key = input("Enter your Alpha Vantage API key: ")

#Separate stock symbols with commas
symbols_input = input("Enter the stock symbols (comma-separated): ")
symbols = [symbol.strip().upper() for symbol in symbols_input.split(',')]

for symbol in symbols:
    stock_prices = get_stock_prices(symbol, api_key)
    if stock_prices is not None:
        insert_data_into_mysql(stock_prices, symbol)
