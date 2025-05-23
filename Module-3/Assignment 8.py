#Justin Marucci
#02/23/2025
#Assignment 8

# Stocks
stocks = {
    'XOM': 110.06,
    'ORCL': 170.87,
    'COST': 999.47,
    'NVO': 91.03,
    'TSLA': 888.97,
    'BRK/A': 450.18,
    'TSM': 200.01,
    'NVDA': 250.63,
    'WMT': 101.01,
    'JPM': 251.23}

# Input ticker symbol
ticker_symbol = input('Enter the ticker symbol: ').upper()

# Searching for ticker symbol
if ticker_symbol in stocks:
    print(f'{ticker_symbol}: ${stocks[ticker_symbol]}')
    # Print not found if ticket symbol is not on list 
else:
    print('not found.')