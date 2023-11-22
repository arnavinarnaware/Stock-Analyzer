# visualize.R
library(ggplot2)
library(RMySQL)

# Replace 'YOUR_API_KEY' with the actual API key
api_key <- 'YOUR_API_KEY'
symbols <- c('AAPL', 'MSFT', 'GOOGL')  # Replace with the symbols from user input

# Connect to the MySQL database
con <- dbConnect(MySQL(), 
                 user='root',
                 password='Password@123',
                 dbname='girrafe',
                 host='localhost')

# Fetch data from the database
df <- dbGetQuery(con, sprintf("SELECT * FROM stock_prices WHERE symbol IN ('%s', '%s', '%s')", symbols[1], symbols[2], symbols[3]))

# Visualization
ggplot(subset(df, symbol %in% symbols), aes(x = date, y = closing_price, color = symbol)) +
  geom_line() +
  labs(x = 'Date', y = 'Closing Price', title = 'Closing Prices Over Time') +
  theme_minimal()

# Close the database connection
dbDisconnect(con)
