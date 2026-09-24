# Data Grokr Week 3 - ETL Pipeline with Unit Tests

## Description

This project implements an ETL (Extract, Transform, Load) pipeline using Python.

The pipeline extracts user data from a REST API in JSON format, processes the data using Python generators and Pandas, transforms the data, and loads the results into CSV and JSON files.

The project also includes automated unit testing using pytest with fixtures and parameterized test cases.


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
- Modular project structure
- Exception handling
- Virtual environment support

## Python Concepts Covered

### Generators and Iterators

- Generator functions
- yield
- Iterators
- Lazy data processing

### REST API and JSON

- REST API requests
- HTTP GET requests
- JSON response processing
- requests library
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
- Fixtures
- Assertions
- Parameterized testing
- Test-driven validation

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