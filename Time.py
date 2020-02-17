import math

hours = int(input('Enter the number of hours:\n'))
minutes = int(input('Enter the number of minutes:\n'))
seconds = int(input('Enter the number of seconds:\n'))

seconds_total = (hours * 3600) + (minutes * 60) + seconds

print('Total seconds:', seconds_total)
