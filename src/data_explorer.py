import pandas as pd
import numpy as np

class ExploratoryDataAnalysis:
    def __init__(self, data):
        self.data = data

    def basic_info(self):
        print("Data shape:", self.data.shape)
        print("Data columns:", self.data.columns)
        print("\nData info:")
        print(self.data.info())
        print("\nData description:")
        print(self.data.describe())

    def analyze_column(self, column_name):
        if column_name in self.data.columns:
            col_data = self.data[column_name]
            print(f"Analyzing column: {column_name}\n")
            print(f"Data type: {col_data.dtype}")
            print(f"Number of unique values: {col_data.nunique()}")
            print(f"Minimum value: {col_data.min()}")
            print(f"Maximum value: {col_data.max()}")
            print(f"Mean value: {col_data.mean()}")
            print(f"Median value: {col_data.median()}")
            print(f"Standard deviation: {col_data.std()}")
            print("\nValue counts:")
            print(col_data.value_counts())
        else:
            print(f"Column '{column_name}' not found in the dataset.")

# Example usage
data = pd.read_csv("your_data.csv")
eda = ExploratoryDataAnalysis(data)
eda.basic_info()
eda.analyze_column("your_column_name")
