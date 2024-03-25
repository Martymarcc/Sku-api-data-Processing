# SKU API Data Processing

This project demonstrates how to consume an API to retrieve Stock Keeping Unit (SKU) data, filter records created on or after January 1, 2022, and save the filtered records to a file. The code is written in Python and utilizes the `requests` library for making HTTP requests to the API.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.x: [Installation Guide](https://www.python.org/downloads/)
- pip (Python package installer): [Installation Guide](https://pip.pypa.io/en/stable/installation/)
- Git: [Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Getting Started

To run the code, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the directory where you want to clone the repository:
   ```bash
   cd /path/to/your/directory

3. Clone this repository to your local machine using the following command:
   'git clone https://github.com/Martymarcc/sku-api-data-processing.git'

4. Navigate to the project directory:
   'cd sku-api-data-processing'

5. Install the required dependencies:
   pip install -r requirements.txt

6. Run the main script:
   python main.py


## Functionality

- The `get_records()` function retrieves records from the provided API.
- The `filter_records(records)` function filters the retrieved records to include only those created on or after January 1, 2022.
- The `count_records(records)` function counts the filtered records.
- The `save_records_to_file(records, filename)` function saves the filtered records to a JSON file.
- The `main()` function orchestrates the entire process, printing the total number of filtered records and saving them to a file.

## File Structure

- `main.py`: Contains the main script to execute the data processing.
- `requirments.txt`: Containts the required libraries 
- `README.md`: This file providing information about the project.
- `filtered_records.json`: File containing all filtered reccords from API



