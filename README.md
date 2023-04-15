# Universal-EDA

Universal-EDA is a Python library that provides an easy-to-use interface for Exploratory Data Analysis (EDA) and data loading. It supports various datasets and helps streamline the EDA process.

## Features

- DataExplorer class: Perform EDA on any dataset, including summary statistics, missing values, and visualization
- DataLoader class: Load common datasets from scikit-learn or convert DataFrames to CSV files

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Universal-EDA (not yet, chatGPT-4 idea).

```bash
pip install universal-EDA
```

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/your_username/universal-EDA.git
cd universal-EDA
pip install -r requirements.txt
```

## Usage


```python
from universal_EDA import DataExplorer, DataLoader

# Load a sample dataset
data_loader = DataLoader()
df = data_loader.load_toy_dataset('iris')

# Perform EDA on the dataset
data_explorer = DataExplorer(df)
data_explorer.summarize()
data_explorer.visualize()

# Save the DataFrame as a CSV file
data_loader.to_csv(df, 'output.csv')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
