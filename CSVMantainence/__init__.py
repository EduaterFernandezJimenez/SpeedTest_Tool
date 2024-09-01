"""
Initialization script for the csvMaintenance package.

This script performs an initial setup by checking if the required CSV file
exists in the specified directory. If the file does not exist, it creates a new
CSV file using the `CSVHandler` class from the `csvMaintenance` package. If
the file is already present, it prints a message indicating that the file
has already been created.

Modules:
    os: Provides functions for interacting with the operating system, including file system operations.
    csvMaintenance.CSVHandler: Custom module for managing CSV file operations, including creation and data appending.

Classes:
    CSVHandler: A class that handles CSV file operations, such as creating a file with headers and adding records.

Functions:
    CSVHandler.file_name: Property that returns the full path of the CSV file used for storing data.
    CSVHandler.create_csv(): Creates a new CSV file with the appropriate headers. If the file already exists, it will be overwritten.
"""


import os
from CSVMantainence import CSVHandler

csv = CSVHandler.CSVHandler()

# Check if the file has been created
if not os.path.exists(csv.file_name):
    csv.create_csv()
else:
    print("The file is already created")