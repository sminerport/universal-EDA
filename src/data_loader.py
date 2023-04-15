import pandas as pd
from sklearn import datasets

class DataLoader:
    def __init__(self):
        self.data = None

    def load_toy_dataset(self, dataset_name):
        if dataset_name == 'boston':
            dataset = datasets.load_boston()
        elif dataset_name == 'iris':
            dataset = datasets.load_iris()
        elif dataset_name == 'diabetes':
            dataset = datasets.load_diabetes()
        # Add more datasets here
        else:
            raise ValueError('Invalid dataset name provided.')

        self.data = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
        self.data['target'] = dataset.target

    def dataframe_to_csv(self, file_name):
        if self.data is not None:
            self.data.to_csv(file_name, index=False)
        else:
            raise ValueError('No data available to save. Load a dataset first.')

# Example usage
data_loader = DataLoader()
data_loader.load_toy_dataset('boston')
data_loader.dataframe_to_csv('boston_dataset.csv')
