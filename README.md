# sku-api-data-processing

# API Data Processing 

This project is designed to demonstrate how to consume data from an API and process it. The provided API is used to manage Stock Keeping Unit (SKU) identifiers for a retail organization. The goal of this project is to retrieve records from the API, filter them based on their creation date, count the filtered records, and save them to a file.

## Requirements

- Python 3.x
- Requests library (can be installed via pip: `pip install requests`)

## Getting Started

To run the code, follow these steps:

1. Clone this repository to your local machine using the following command:
   'git clone https://github.com/Martymarcc/sku-api-data-processing.git'

2. Navigate to the project directory:
   'cd sku-api-data-processing'

3. Install the required dependencies:
   pip install -r requirements.txt

4. Run the main script:
   python main.py


## Functionality

- The `get_records()` function retrieves records from the provided API.
- The `filter_records(records)` function filters the retrieved records to include only those created on or after January 1, 2022.
- The `count_records(records)` function counts the filtered records.
- The `save_records_to_file(records, filename)` function saves the filtered records to a JSON file.
- The `main()` function orchestrates the entire process, printing the total number of filtered records and saving them to a file.

## File Structure

- `main.py`: Contains the main script to execute the data processing.
- `README.md`: This file providing information about the project.
- `filtered_records.json`: JSON file containing the filtered records saved by the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


