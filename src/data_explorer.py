"""
"ExploratoryDataAnalysis" module is used to provide basic visualizations to summarize and analyze the provided data efficiently by outputing
  data's description, columns and structure information. Also, this module is capable of obtaining a given column's data type,
 the number of unique values, mean value, median value and  standard deviation.

Class :
ExploratoryDataAnalysis:
    Parameters:
    data(array-like): Data to be initialized with.

Methods:
basic_info(): Dispaly basic info of a given dataset such as data's shape, columns and
             structure.

analyze_column(column_name): Analyzes the given column and prints information such as
                the dataset's data type, the number of unique values, mean
                value, median value and standard deviation.

Note:
    The given column must exist in the dataset otherwise an error message is provided by this module.

Raises:
   None
"""
import pandas as pd
import numpy as np


class ExploratoryDataAnalysis:
    """
    Registers an object to receive basic and detailed data exploration.

        Class ExploratoryDataAnalysis, which receives as its parameter only the received data, and determines
        simpler visualizations to summarize basic details and understand data characteristics
        (eg shape, field, structure).

        Parameters
        ----------
        data : array-like
            Data to be initialized with.

        Methods
        -------
        basic_info()
            Display basic info of a given     dataset such as data's shape, columns and structure.

        analyze_column(column_name)
               Prints information helpful for data analysis on the visible column in a member object, this
               such as it's data type, total number of unique values, mean, median, standard deviation and
               distribution of values,informations.

        Raises
        ------
        None
    """

    def __init__(self, data):
        """
        Initializes the object with given data.

        Parameters
        ----------
        data : array-like
            Data to be initialized with.
        """

        self.data = data

    def basic_info(self):
        """
        Dispaly basic info of a given dataset such as data's shape, columns and structure.

        Parameters
        ----------
        self: Pandas DataFrame
            The dataset to which basic info is applied

        Returns
        -------
        None
        """

        print("Data shape:", self.data.shape)
        print("Data columns:", self.data.columns)
        print("\nData info:")
        print(self.data.info())
        print("\nData description:")
        print(self.data.describe())

    def analyze_column(self, column_name):
        """
        This function prints information helpful for data analysis on the given column in a provided dataset, such
        as it's data type, total number of unique values, mean, median, standard deviation, and distribution of values,
        namely.

        Parameters
        ----------
        self [object] : An instance of a class containing the data.
        column_name [string]: The column name corresponding to the data that needs to be analyzed.

        Notes
        -----
        If the given column_name does not exist in the dataset, a corresponding
        message is printed.

        Returns
        -------
        None
        """

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


if __name__ == "__main__":
    data = pd.read_csv("boston_dataset.csv")
    eda = ExploratoryDataAnalysis(data)
    eda.basic_info()
    eda.analyze_column("target")
