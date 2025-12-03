import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print("API request failed:", response.status_code)
    exit()

df = pd.DataFrame(data)

print("---- Data collected from REST API ----")
print(df)
