# Write a Python function that calculates the uptime percentage of a service based on the total number of hours and the number of hours the service was down. 
# The function should take 2 parameters(total hours and down hours, inputted when the function is run). 
# Lastly, the function should return the uptime percentage rounded to two decimal places. 

# Uptime percentage equation = (Total time - Downtime) / Total time x 100

# Function that takes totalHours and downHours as parameters
# (parameters must be inputted in minutes)
def runtime(totalHours, downHours):
    uptime = (totalHours - downHours)
    division = (uptime / totalHours)
    answer = (division * 100)
    print(round(answer, 2))

runtime(1440,60)
