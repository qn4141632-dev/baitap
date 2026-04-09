import time

# Get current time in seconds since epoch
current_time = time.time()

# Calculate days since epoch
days_since_epoch = int(current_time // (24 * 3600))

# Calculate hours, minutes, seconds of current day
seconds_today = int(current_time % (24 * 3600))
hours = seconds_today // 3600
minutes = (seconds_today % 3600) // 60
seconds = seconds_today % 60

print("Days since epoch:", days_since_epoch)
print("Current time of day: {:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
