import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

#Replace 'YOUR_API_KEY' with personal API key
api_key = 'YOUR_API_KEY'
symbols = ['AAPL', 'MSFT', 'GOOGL']  # Replace with stock symbols

#Connect to MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Password@123',
    database='girrafe'
)

if connection.is_connected():
    cursor = connection.cursor()

    #Get data from database
    df = pd.read_sql("SELECT * FROM stock_prices WHERE symbol IN (%s, %s, %s)", params=tuple(symbols), con=connection, parse_dates=['date'])

    #visualization of prices
    for symbol in symbols:
        df_symbol = df[df['symbol'] == symbol]
        plt.plot(df_symbol['date'], df_symbol['closing_price'], label=symbol)

    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Closing Prices Over Time')
    plt.legend()
    plt.show()

    cursor.close()
    connection.close()
