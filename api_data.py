import requests
import pandas as pd
import os

data_list = []

# Loop through first 10 Star Wars characters
for i in range(1, 11):
    url = f"https://swapi.dev/api/people/{i}/"
    response = requests.get(url)
    data = response.json()

    data_list.append({
        "Name": data.get("name"),
        "Height": data.get("height"),
        "Mass": data.get("mass"),
        "Gender": data.get("gender")
    })

# Convert to DataFrame
df = pd.DataFrame(data_list)

# Save CSV in SAME folder
csv_path = os.path.abspath("swapi_data.csv")
df.to_csv(csv_path, index=False)

print("Star Wars characters data collected!")
print("CSV saved at:", csv_path)
print(df.head())
