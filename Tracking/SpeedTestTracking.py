"""
Internet Speed Measurement and Tracking Script.

This script provides functionality to measure internet download speed
using the `speedtest` library and logs the results to a CSV file. It includes
methods for performing individual speed measurements as well as continuous
tracking at specified intervals.

Modules:
    speedtest: A library for testing internet bandwidth using Speedtest.net.
    time: Provides various time-related functions.
    socket: Provides access to the network interface and allows socket-based communication.
    csvMaintenance.CSVHandler: Custom module for handling CSV file operations.

Classes:
    SpeedTestTracking: A class that encapsulates functionality for measuring
                       and tracking internet speed.

Methods:
    _measure_speed(): Measures and logs the internet download speed, handling any errors.
    velocity_tracking(interval=30): Continuously tracks and prints download speed at specified intervals.

Usage:
    - Create an instance of `SpeedTestTracking`.
    - Call `_measure_speed()` to perform a single speed test and log the result (typically called within `velocity_tracking()`).
    - Call `velocity_tracking(interval)` to continuously track and log internet speed at the specified interval.
"""


import speedtest
import time
import socket
from CSVMantainence import CSVHandler

class SpeedTestTracking:

    def __init__(self):
        self._csv_Handler = CSVHandler.CSVHandler()

    def _measure_speed(self):
        """
        Measures the internet download speed and logs the result.

        This method uses the `speedtest` library to determine the best server and
        measure the download speed in megabits per second (Mbps). The result is
        logged along with the timestamp and status in a CSV file. If the measurement
        fails due to a connection issue or other errors, it logs the error details
        and returns `None`.

        Returns:
            float: The download speed in Mbps if successful, otherwise `None`.

        Exceptions:
            speedtest.SpeedtestBestServerFailure: Raised if the best server selection fails.
            socket.timeout, socket.gaierror: Raised in case of network errors, such as timeout or
                                              connection issues.
            Exception: Catches any other unexpected errors.
        """

        try:
            st = speedtest.Speedtest()
            st.get_best_server()  # Choose the best server
            download_speed = st.download() / 10 ** 6  # Convert a MB/s
            data = [time.strftime("%Y-%m-%d %H:%M:%S"), download_speed, "OK"]
            self._csv_Handler.add_records(data)
            return download_speed
        except speedtest.SpeedtestBestServerFailure as e:
            print(f"Error: Could not connect to the servers to measure latency. Details: {e}")
            data = [time.strftime("%Y-%m-%d %H:%M:%S"), 0, "BAD REQUEST", e]
            self._csv_Handler.add_records(data)
            return None
        except (socket.timeout, socket.gaierror) as e:
            print(f"Network error: Cannot connect to server. Possible router reset or connection problem. Details: {e}")
            data = [time.strftime("%Y-%m-%d %H:%M:%S"), 0, "BAD REQUEST", e]
            self._csv_Handler.add_records(data)
            return None
        except Exception as e:
            print(f"Unexpected error when measuring speed: {e}")
            data = [time.strftime("%Y-%m-%d %H:%M:%S"), 0, "BAD REQUEST", e]
            self._csv_Handler.add_records(data)
            return None

    def velocity_tracking(self, interval=30):
        """
        Continuously tracks and prints the internet download speed at specified intervals.

        This method calls `_measure_speed()` in a loop to measure the download speed
        and prints the result to the console. If the speed cannot be measured, it
        notifies the user. The tracking continues indefinitely until interrupted by the user.

        Args:
            interval (int, optional): The time interval (in seconds) between each
                                      speed measurement. Default is 30 seconds.

        Exceptions:
            KeyboardInterrupt: Raised when the user interrupts the tracking process,
                               typically by pressing Ctrl+C. The method will then
                               gracefully terminate the loop and print a finishing message.
        """
        try:
            while True:
                velocity = self._measure_speed()
                if velocity is not None:
                    print(f"Download speed: {velocity:.2f} MB/s")
                else:
                    print("Speed could not be measured at this time.")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Tracking finished.")
