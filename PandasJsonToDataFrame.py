import requests
import pandas as pd
import numpy as np
import json

# URL in the exercise does not work, have to use this URL
api_url = "https://api.marketdata.app/v1/stocks/candles/D/AAPL?from=2022-01-01&to=2022-12-31"

# Get Response 
response = requests.get(api_url)
#print (response.json())


# Parse JSON data - no needed
#data = json.loads(response.json())

# Convert to DataFrame
df = pd.DataFrame(response.json())

# Display the DataFrame last 10 rows
#print(df)
print(df.tail(10))




