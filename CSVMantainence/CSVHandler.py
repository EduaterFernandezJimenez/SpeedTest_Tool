"""
CSV management utility for tracking internet speed.

This class provides methods to manage a CSV file used for logging internet
speed data. It includes functionality to create the CSV file with appropriate
headers, add records to the file, and retrieve the file name.

Attributes:
    _file_name (str): The name of the CSV file where data is stored.

Usage:
    This class is designed to be used as part of a larger application that
    tracks and logs internet speed data over time.
"""

import csv


class CSVHandler:

    def __init__(self):
        self._file_name = 'internet_speed.csv'

    @property
    def file_name(self):
        """
        Returns the name of the CSV file.

        This property retrieves the name of the CSV file that is used to store
        the internet speed data.

        Returns:
            str: The name of the CSV file.
        """
        return self._file_name

    def create_csv(self):
        """
        Creates the CSV file with the appropriate headers.

        This method creates a new CSV file with the specified file name and adds
        the headers: ['Timestamp', 'Speed_MB/s', 'Status', 'ERROR']. If the file
        already exists, it will be overwritten.

        Side Effects:
            A new CSV file is created in the current directory.

        Prints:
            A message indicating that the file has been successfully created.
        """
        with open(self._file_name, mode='w', newline='') as csv_file:
            writer_csv = csv.writer(csv_file, delimiter=';')
            writer_csv.writerow(['Timestamp', 'Speed_MB/s', 'Status', 'ERROR'])
        print(f"File {self._file_name} successfully created.")

    def add_records(self, data):
        """
        Appends a new record to the CSV file.

        This method adds a new row to the existing CSV file. The row should
        contain data in the format: [timestamp, speed, status, error].

        Args:
            data (list): A list containing the record data to be added to the CSV file.

        Side Effects:
            The provided data is appended as a new row in the CSV file.
        """
        with open(self._file_name, mode='a', newline='') as csv_file:
            writer_csv = csv.writer(csv_file, delimiter=";")
            writer_csv.writerow(data)