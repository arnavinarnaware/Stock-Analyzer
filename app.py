from flask import Flask, render_template, request, redirect, url_for
from stock_analysis import get_stock_prices, insert_data_into_mysql

app = Flask(__name__)

# index route
@app.route('/')
def index():
    return render_template('index.html')

# submit route
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        api_key = request.form['api_key']
        symbols_input = request.form['symbols']
        symbols = [symbol.strip().upper() for symbol in symbols_input.split(',')]

        for symbol in symbols:
            stock_prices = get_stock_prices(symbol, api_key)
            if stock_prices is not None:
                insert_data_into_mysql(stock_prices, symbol)

        return redirect(url_for('index'))

    return render_template('index.html', error="Error fetching or inserting data. Please try again.")

# Run app when script is executed
if __name__ == '__main__':
    app.run(debug=True)
