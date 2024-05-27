# Importing necessary modules
import pandas as pd
import os
import argparse

# Implemented code to read my dataset file
file_path = 'dataset.csv'
data = pd.read_csv(file_path)

# Displayingg the first few rows of the DataFrame to verify that the data was read correctly
print(data.head())

num_rows, num_cols = data.shape
num_features = data.columns.tolist()

print("Dataset Description:")
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")
print(f"Available features: {num_features}")

# Displayed a sample of the dataset
print("\nSample of the dataset:")
print(data.head())
def display_dataset(dataset, columns=None, num_rows=None):
    header = dataset[0]
    data = dataset[1:]
    
    # If else conditions for filtering columns
    if columns:
        column_index = [i for i, column in enumerate(header) if column in columns]
        if column_index:
            filtered_data = [[row[i] for i in column_index] for row in data]
            filtered_header = [header[i] for i in column_index]
            df = pd.DataFrame(filtered_data, columns=filtered_header)
            if num_rows:
                df = df.head(num_rows)
            print(df)
        else:
            print("No matching columns found.")
    elif num_rows:
        if num_rows > len(data):
            num_rows = len(data)
        df = pd.DataFrame(data, columns=header)
        df = df.head(num_rows)
        print(df)
    else:
        df = pd.DataFrame(data, columns=header)
        print(df)

# While loading data to implement error handling 
def load_dataset(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: Dataset file '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error occurred while loading the dataset: {e}")
        return None

def display_dataset(dataset, columns=None, num_rows=None):
    """
    Display the dataset.

    Parameters in the dataset:
    - Dataset: DataFrame, the dataset to display.
    - Columns: list or None, list of columns to display. If None, display all columns.
    - Number of rows: int or None, number of rows to display. If None, display all rows.
    """
    if dataset is None:
        print("No dataset to display.")
        return

    if columns:
        dataset = dataset[columns]
    if num_rows:
        dataset = dataset.head(num_rows)
    print(dataset)


# Cleaning the dataset
def clean_dataset(dataset):
    """
    Clean the dataset by handling missing values and performing data transformations.
    
    Parameters:
        dataset (DataFrame): Input dataset.
    
    Returns:
        DataFrame: Cleaned dataset.
    """
    # Handle missing values
    dataset.dropna(inplace=True)

    # Perform data transformations if necessary (e.g., convert data types)

    return dataset

def main():
    # Detecting the dataset file
    script_directory = os.path.dirname(os.path.realpath(__file__))
    dataset_file = os.path.join(script_directory, 'dataset.csv')

    dataset = load_dataset(dataset_file)

    if dataset is None:
        return

    # Parsing command-line arguments
    parser = argparse.ArgumentParser(description='CLI for interacting with dataset.')
    parser.add_argument('--search', nargs='+', help='Search for specific columns.')
    parser.add_argument('--rows', type=int, help='Number of rows to display.')
    args = parser.parse_args()

    # Display the dataset after the change 
    display_dataset(dataset, columns=args.search, num_rows=args.rows)

if __name__ == '__main__':
    main()
