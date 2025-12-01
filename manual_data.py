import os
import pandas as pd

# Create Data
data = {
    "name": ["Rohan", "Priya", "Kabir", "Sneha", "Vivek", "Tanya", "Harsh", "Divya", "Meera"],
    "age": [22, 19, 24, 21, 18, 23, 20, 26, 28],
    "gender": ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'F'],
    "Education": ["BBA", "BA", "BSc", "MBA", "12th", "BCA", "MCom", "MA", "PhD"]
}

df = pd.DataFrame(data)

# Save CSV in the same directory as the script
csv_path = os.path.join(os.path.dirname(__file__), "manual_data.csv")
df.to_csv(csv_path, index=False)

print("CSV Created Successfully At:")
print(csv_path)
print(df.head())
