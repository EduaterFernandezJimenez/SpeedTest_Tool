from Tracking import SpeedTestTracking

if __name__ == '__main__':
  time_interval = 60  # Time interval in seconds between each medication
  tr = SpeedTestTracking.SpeedTestTracking()
  tr.velocity_tracking(time_interval)