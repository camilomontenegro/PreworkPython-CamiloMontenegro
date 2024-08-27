import yfinance as yf

def get_exchange_rate():
  data = yf.Ticker("USDEUR=X")
  todays_data = data.history(period='1d')

  exchange_rate = todays_data['Close'].iloc[0]
  return exchange_rate

def convert(usd):
  exchange_rate = get_exchange_rate()
  eur = usd * exchange_rate
  return eur 

usd_amount = float(input("Enter amount in USD: "))
eur_amount = convert(usd_amount)
print(f'{usd_amount} USD is equivalent to {eur_amount: .2f} EUR at the current exchange rate.')