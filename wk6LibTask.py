#Author: Moleboheng Madela
#Date: 2025-05-05

# Importing the required libraries
import numpy as np                # NumPy is used for numerical operations like arrays and statistics
import pandas as pd               # Pandas is used for working with tabular data
import matplotlib.pyplot as plt   # Matplotlib is used for plotting charts and graphs
import requests                   # Requests is used to make HTTP requests to APIs

# Task 1: Create a NumPy array and calculate the mean
array = np.arange(1, 11)  # Creates an array with numbers from 1 to 10 (inclusive)
mean_value = np.mean(array)  # Calculates the mean (average) of the array
print("NumPy Array:", array)  # Prints the array
print("Mean of array:", mean_value)  # Prints the mean value

# Task 2: Load a small dataset into a pandas DataFrame and display summary statistics
# Creating a simple dataset as a dictionary
data = {
    'Name': ['Lebo', 'Nini', 'Khido', 'Fifi'],
    'Age': [31, 30, 35, 36],
    'Height': [165, 170, 164, 162]
}

# Converting the dictionary to a pandas DataFrame
df = pd.DataFrame(data)
print("\nPandas DataFrame:\n", df)  # Displaying the full table

# Generating and printing summary statistics for numeric columns (Age, Salary)
print("\nSummary Statistics:\n", df.describe())

# ✅ Task 3: Fetch data from a public API using requests
# Making a GET request to the CoinDesk API to fetch Bitcoin price data
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# Checking if the response was successful (status code 200 means OK)
if response.status_code == 200:
    btc_data = response.json()  # Converting the response to a JSON (dictionary) format
    usd_rate = btc_data['bpi']['USD']['rate']  # Extracting the Bitcoin price
