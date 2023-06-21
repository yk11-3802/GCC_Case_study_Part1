import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataframes
actuals = pd.read_csv("Actuals.csv")
price = pd.read_csv("Price.csv")
bcr = pd.read_csv("B&CR.csv")

# Clean the data
actuals = actuals.dropna()
price = price.dropna()
bcr = bcr.dropna()

# Merge the dataframes
merged_data = pd.merge(actuals, price, on=["Material Number", "Plant"])
merged_data = pd.merge(merged_data, bcr, on=["Material Number"])
#print(merged_data)

merged_data = merged_data.reset_index(drop=True)
merged_data.columns = merged_data.columns.str.strip()

# Calculate the Bottle Rands and Crate Rands columns
merged_data['Bottle Rands'] = merged_data['Price per case'].mul(2)
merged_data['Crate Rands'] = merged_data['Amount in LC'].mul(2)

# Perform variance analyses
#variance_by_plant = merged_data.groupby("Plant")["Actuals", "Target"].agg(lambda x: x.diff())
#variance_by_category = merged_data.groupby("Category")["Actuals", "Target"].agg(lambda x: x.diff())

# Perform trend analysis
#plt.plot(merged_data["Actuals"], label="Actuals")
#plt.plot(merged_data["Target"], label="Target")
#plt.legend()
#plt.show()

# Save the results
merged_data.to_csv("consolidated_data.csv")
