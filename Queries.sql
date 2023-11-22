-- for only one stock symbol
CREATE TABLE stock_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    symbol VARCHAR(10),
    closing_price DECIMAL(10, 2)
);

-- modify table to allow it to store multiple data for multiple stock symbols
-- create a company_id column as a foreign key for the companies table
CREATE TABLE stock_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    symbol VARCHAR(10),
    closing_price DECIMAL(10, 2),
    company_id INT AUTO_INCREMENT,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);


SELECT * FROM stock_prices;

SELECT * FROM stock_prices WHERE symbol = 'GOOG';

SELECT * FROM stock_prices WHERE date BETWEEN '2023-06-27' AND '2023-06-30';

SELECT symbol, AVG(closing_price) AS average_closing_price FROM stock_prices GROUP BY symbol;


DELETE FROM stock_prices;

CREATE TABLE companies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO companies (name) VALUES
('Apple Inc.'),
('Microsoft Corporation'),
('Google LLC');

SELECT * FROM companies;

--calculate the daily percentage change in closing prices for each stock symbol
SELECT
    date,
    symbol,
    closing_price,
    (closing_price - LAG(closing_price) OVER (PARTITION BY symbol ORDER BY date)) / LAG(closing_price) OVER (PARTITION BY symbol ORDER BY date) * 100 AS daily_percentage_change
FROM stock_prices
ORDER BY symbol, date;

--only get the latest closing prices:
SELECT symbol, MAX(date) AS latest_date, closing_price
FROM stock_prices
GROUP BY symbol;




