import math

seconds = int(input('Enter the number of seconds:\n'))
hours = seconds // 3600
remainder = seconds % 3600
minutes = remainder // 60
seconds_remaining = remainder % 60

print('Hours:', hours)
print('Minutes:', minutes)
print('Seconds:', seconds_remaining)
