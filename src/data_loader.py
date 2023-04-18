"""
A module for loading and saving given toy datasets for item
classification tasks.


Attributes:
- data (Pandas.DataFrame): DataFrame containing all the selected toy dataset.

Methods
- load_toy_dataset(dataset_name: str):  Loads a specified toy dataset.
- dataframe_to_csv(file_name: str): Saves a given DataFrame to a csv file.


Raises:
ValueError: Raised when an invalid dataset name is passed.
"""
import pandas as pd
from sklearn import datasets


class DataLoader:
    """
    The DataLoader class loads toy datasets for practice and experimentation.
    It also contains methods for saving data to CSV file.

    Parameters
    ----------
    dataset_name : str
            Name of the dataset to be loaded. Possible values are:
            {'boston', 'iris', 'diabetes'}.

    Attributes
    ----------
    data : Pandas.DataFrame
            DataFrame containing all the selected toy dataset.

    file_name : str
            Name of the csv file, where the extracted dataset must be
            saved.

    Methods
    -------
    load_toy_dataset
            Selects and loads the toy dataset, with given dataset_name.

    dataframe_to_csv
            Takes the dataframe as input and save the csv to 'file_name'.

    Raises
    ------
    ValueError
    """

    def __init__(self):
        """
        Constructor initializing `data` attribute.

        Parameters
        ----------
        self : object
            Instance of the class.

        Attributes
        ----------
        data : Object
            Data of the class.
                self.data = None
        """
        self.data = None

    def load_toy_dataset(self, dataset_name):
        """
        Load Toy machine learning dataset

        Parameters
        ----------
        dataset_name : str
            The name of the dataset that has to be loaded.

        Returns
        -------
        data : pd.DataFrame
            A DataFrame containing the loaded dataset.

        Raises
        ------
        ValueError : If an invalid dataset name is passed.
        """

        if dataset_name == "boston":
            dataset = datasets.load_boston()
        elif dataset_name == "iris":
            dataset = datasets.load_iris()
        elif dataset_name == "diabetes":
            dataset = datasets.load_diabetes()
        elif dataset_name == "digits":
            dataset = datasets.load_digits()
        elif dataset_name == "linnerud":
            dataset = datasets.load_linnerud()
        elif dataset_name == "wine":
            dataset = datasets.load_wine()
        elif dataset_name == "breast_cancer":
            dataset = datasets.load_breast_cancer()
        else:
            raise ValueError("Invalid dataset name provided.")

        if dataset_name == "linnerud":
            data = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
            data["target"] = [tuple(x) for x in dataset.target]
            data["target_names"] = [tuple(x) for x in dataset.target_names]
        else:
            data = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
            data["target"] = dataset.target

        self.data = data
        return data

    def dataframe_to_csv(self, file_name):
        """
        Export given DataFrame to a csv file.

        Parameters
        ----------
        file_name : str
            The name of the file the DataFrame data should be saved to

        Raises
        ------
        ValueError
            If DataFrame data is not provided and no data to save
                if self.data is not None:
                    self.data.to_csv(file_name, index=False)
                else:
                    raise ValueError("No data available to save. Load a dataset first.")
        """
        if self.data is not None:
            self.data.to_csv(file_name, index=False)
        else:
            raise ValueError("No data available to save. Load a dataset first.")


if __name__ == "__main__":
    # Example usage
    data_loader = DataLoader()
    data_loader.load_toy_dataset("boston")
    data_loader.dataframe_to_csv("boston_dataset.csv")
