import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

end_date = datetime.today()
start_date = end_date - timedelta(days=6)

# Download historical data for the financial instrument
data = yf.download('GBPUSD=X', start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'), interval='5m')

# Remove timezone information and format the date to include hours, minutes, and seconds
data.index = data.index.tz_localize(None).strftime('%Y-%m-%d %H:%M:%S')

# Save to CSV
data.to_csv('GBPUSD_5M_7_days.csv')

print("Data saved to GBPUSD_5M_7_days.csv")