import requests
import pandas as pd
import mysql.connector

def get_stock_prices(symbol, api_key):
    base_url = "https://www.alphavantage.co/query"
    function = "TIME_SERIES_DAILY"
    datatype = "json"

    params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key,
        "datatype": datatype,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  #raise HTTPError

        data = response.json()["Time Series (Daily)"]
        df = pd.DataFrame(data).T
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        return df
    except requests.exceptions.RequestException as e:
        print(f"Error fetching stock data for {symbol}: {e}")
        return None

def insert_data_into_mysql(data, symbol):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Password@123',
        database='girrafe'
    )

    if connection.is_connected():
        try:
            cursor = connection.cursor()

            for date, row in data.iterrows():
                query = "INSERT INTO stock_prices (date, symbol, closing_price) VALUES (%s, %s, %s)"
                cursor.execute(query, (date, symbol, row['4. close']))

            connection.commit()
            print(f"Data for {symbol} inserted into MySQL database")

        except mysql.connector.Error as err:
            print(f"Error inserting data into MySQL database for {symbol}: {err}")

        finally:
            cursor.close()
            connection.close()

#ex
if __name__ == "__main__":
    api_key = 'YOUR_API_KEY'  #use personal API key
    symbols = ['AAPL', 'MSFT', 'GOOGL'] 

    for symbol in symbols:
        stock_prices = get_stock_prices(symbol, api_key)
        if stock_prices is not None:
            insert_data_into_mysql(stock_prices, symbol)
