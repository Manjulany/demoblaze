# BDD Selenium Python Test Project For Demoblaze

## Description
This project uses Selenium and Python with BDD (Behavior-Driven Development) to automate web testing. It includes test scenarios written in Gherkin syntax and executed using the Behave framework.

## Table of Contents
- Installation
- Usage
- Project Structure
- Running Tests

## Installation
1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
   
    unzip <project_archive>.zip
    cd <project_directory>
   
2. **Create a virtual environment**:
    ```bash
   python -m venv venv
   source venv/bin/activate  
   `venv\Scripts\activate` # On Windows
   
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   
   Allure Report installation and setup
   https://allurereport.org/docs/install/
   
4. **Download and update browser drivers**: Ensure the appropriate browser drivers (e.g., ChromeDriver) are in your system’s PATH.


### Usage
Use of project, including any necessary configurations.

    1. **Configure the environment**:
        Edit the `environment.py` file to set up any necessary environment variables or configurations.

    2. **Write your test scenarios**:
        Add your feature files in the `features` directory using Gherkin syntax.

    3. **Run the tests**:
        ```bash
           behave

### Project Structure

    ## Project Structure
        .
        ├── features
        │   ├── pages
        │   ├── steps
        │   ├── environment.py
        │   └── *.feature
        ├── allure-report
        ├── reports
        ├── runner
        ├── config
        ├── requirements.txt
        └── README.md

## Running Tests
1. **To run all tests:**
    ```bash
   python test_runner/test_runner.py
   ```
   
2. **To run a specific feature file:**
   ```bash
   python test_runner/test_runner.py features/<feature_file>.feature
   ```
3. **To run tests with a specific tag:**
   ```bash
    python test_runner/test_runner.py --tags=@tag_name
    ```
   