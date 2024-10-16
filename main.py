import csv

def count_data_in_columns(csv_file):
    # Initialize dictionaries to count data, empty rows, and sum for each column
    column_data_count = {}
    column_empty_count = {}
    column_sum = {}
    total_rows = 0  # To keep track of the total number of rows

    # Open the CSV file
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Get the column headers

        # Initialize counts and sums for each column
        for header in headers:
            column_data_count[header] = 0
            column_empty_count[header] = 0
            column_sum[header] = 0

        # Iterate over each row in the CSV file
        for row in reader:
            total_rows += 1  # Increment total row count
            for i, value in enumerate(row):
                if value.strip():  # If the cell has data (not empty or just spaces)
                    column_data_count[headers[i]] += 1
                    try:
                        # Try to convert the value to a float and sum it if it's numeric
                        column_sum[headers[i]] += float(value.replace(',', '.'))  # Replace comma with dot if needed
                    except ValueError:
                        pass  # Skip if it's not a number
                else:
                    column_empty_count[headers[i]] += 1

    # Display the counts, percentages, and averages
    print(f"Total number of rows: {total_rows}\n")

    print("Data count, percentage of missing data, and average per column:")
    for column in headers:
        data_count = column_data_count[column]
        empty_count = column_empty_count[column]
        missing_percentage = (empty_count / total_rows) * 100 if total_rows > 0 else 0
        avg_value = (column_sum[column] / data_count) if data_count > 0 else 'N/A'
        print(f"{column}: {data_count} data, {empty_count} empty, {missing_percentage:.2f}% missing, average = {avg_value}")

# Example usage
csv_file_path = 'code_postal/code_postal_25000_2023.csv'
count_data_in_columns(csv_file_path)