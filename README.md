# Data Grokr Week 3 - ETL Pipeline with Unit Tests

## Objective

The objective of this project is to develop a complete ETL pipeline that extracts JSON data from a REST API, processes the data using Python generators and Pandas, transforms the data into a structured format, and loads the results into CSV and JSON files.

The project also demonstrates automated unit testing using pytest, fixtures, and parameterized test cases.

## Description

This project implements an ETL (Extract, Transform, Load) pipeline using Python.

The pipeline extracts user data from a REST API in JSON format, processes the data using Python generators and Pandas, transforms the data, and loads the results into CSV and JSON files.

The project also includes automated unit testing using pytest.


## ETL Pipeline

The project follows the following flow:

REST API
↓
JSON Data
↓
Python Generator
↓
Pandas Transformation
↓
CSV + JSON Output

## Features

- Fetch data from a REST API
- Process JSON response data
- Use Python generators for lazy processing
- Transform data using Pandas
- Calculate additional data fields
- Group and summarize data
- Export transformed data to CSV
- Export summary data to JSON
- Automated unit testing using pytest
- Pytest fixtures
- Parameterized tests
- Exception handling
- Modular project structure
- Virtual environment support

## Python Concepts Covered

### Generators and Iterators

- Generator functions
- `yield`
- Iterators
- Lazy data processing

### REST API and JSON

- REST API requests
- HTTP GET requests
- JSON response processing
- `requests` library
- API error handling

### Pandas

- DataFrame creation
- Data transformation
- String operations
- GroupBy
- CSV export

### Unit Testing

- pytest
- Test functions
- Assertions
- Fixtures
- Parameterized testing

## Technologies Used

- Python
- Requests
- Pandas
- Pytest
- JSON
- REST API
- Git
- GitHub
- Visual Studio Code

## Project Structure

```text
DATAGROKR-Week3-ETL-Pipeline-with-Unit-Tests/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── etl/
│   ├── __init__.py
│   ├── api.py
│   ├── transform.py
│   └── pipeline.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_etl.py
│
└── output/
    ├── users_transformed.csv
    └── city_summary.json
```

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Sameer-Honnatti/DATAGROKR-Week3-ETL-Pipeline-with-Unit-Tests.git
```

### 2. Open the Project Folder

```bash
cd DATAGROKR-Week3-ETL-Pipeline-with-Unit-Tests
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the ETL Pipeline

```bash
python main.py
```

### 7. Run Unit Tests

```bash
pytest
```

## Testing

The project uses pytest for automated unit testing.

The test suite covers:

- Generator functionality
- Pandas data transformation
- Data summarization
- ETL pipeline processing
- Email domain processing
- Pytest fixtures
- Parameterized test cases

### Test Result

All 7 tests passed successfully.

```text
7 passed
```

## Sample Output

### ETL Pipeline Output

```text
=======================================================
       DATA GROKR WEEK 3 - ETL PIPELINE
=======================================================

ETL pipeline completed successfully.
Output file: output\users_transformed.csv
```

### Pytest Output

```text
7 passed
```

## Output Files

### users_transformed.csv

The `users_transformed.csv` file contains the transformed user dataset with additional fields.

The dataset contains:

- ID
- Name
- Username
- Email
- City
- Company
- Name Length
- Email Domain
- City Uppercase

### city_summary.json

The `city_summary.json` file contains the number of users grouped by city.

## Learning Outcomes

Through this project, the following concepts were practiced:

- Building an ETL pipeline using Python
- Consuming REST APIs
- Processing JSON data
- Using generators and iterators
- Performing data transformation using Pandas
- Creating CSV and JSON output files
- Writing automated unit tests
- Using pytest fixtures
- Using parameterized tests
- Organizing Python projects into modules and packages
- Managing dependencies using virtual environments
- Handling errors and exceptions
- Using Git and GitHub for version control

## Author

**Sameer Honnatti**

Artificial Intelligence and Data Science

Nitte Meenakshi Institute of Technology