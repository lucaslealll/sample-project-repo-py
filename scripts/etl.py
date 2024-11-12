import pandas as pd


def extract(file_path):
    """
    Extract data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file to read.

    Returns:
    pd.DataFrame: The extracted data.
    """
    try:
        data = pd.read_csv(file_path)
        print("Data extraction successful")
        return data
    except Exception as e:
        print(f"Error during extraction: {e}")


def transform(data):
    """
    Transform the data.

    Parameters:
    data (pd.DataFrame): The data to transform.

    Returns:
    pd.DataFrame: The transformed data.
    """
    try:
        # Example transformation: convert all column names to lowercase
        data.columns = [col.lower() for col in data.columns]

        # Example transformation: remove rows with missing values
        data = data.dropna()

        # Example transformation: add a new column 'total' which is the sum of all numeric columns per row
        numeric_cols = data.select_dtypes(include="number").columns
        data["total"] = data[numeric_cols].sum(axis=1)

        print("Data transformation successful")
        return data
    except Exception as e:
        print(f"Error during transformation: {e}")


def load(data, output_file_path):
    """
    Load the data into a CSV file.

    Parameters:
    data (pd.DataFrame): The data to load.
    output_file_path (str): The path to the output CSV file.
    """
    try:
        data.to_csv(output_file_path, index=False)
        print("Data loading successful")
    except Exception as e:
        print(f"Error during loading: {e}")


def main():
    input_file_path = "input_data.csv"  # Path to the input CSV file
    output_file_path = "output_data.csv"  # Path to the output CSV file

    # Extract
    data = extract(input_file_path)

    if data is not None:
        # Transform
        transformed_data = transform(data)

        if transformed_data is not None:
            # Load
            load(transformed_data, output_file_path)


if __name__ == "__main__":
    main()
