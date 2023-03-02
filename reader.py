# # Log in to https://www.esbnetworks.ie/ and go to the "My Account" page

# import requests
# from bs4 import BeautifulSoup

# # Log in to the website
# session_requests = requests.session()
# LOGIN_URL = "https://www.esbnetworks.ie/login"
# result = session_requests.get(LOGIN_URL)
# soup = BeautifulSoup(result.text, "html.parser")
# authenticity_token = soup.find("input", {"name": "authenticity_token"})["value"]    # Get the authenticity token
# payload = {
#     "authenticity_token": authenticity_token,
#     "user[email]": "daniel.cregg@gmail.com",    # Replace with your email address
# }

# Read the data from a csv file that begins with HDF_ and ends with .csv
# The file should be in the same directory as this script   
# The file should contain the following columns: MPRN,Meter Serial Number,Read Value,Read Type,Read Date and End Time
# Create a graph of the data in the cloumn named "Read Value" against the date and time in the column named "Read Date and End Time"
# The graph should be saved as a png file in the same directory as this script

import csv
import datetime
from logging import log
import matplotlib.pyplot as plt

with open('HDF_10020162832_02-03-2023.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots)    # Skip the first row of the csv file
    for row in plots:
        # Get the date and time from the csv file and convert it to a datetime object
        date_time_str = row[4]
        x = datetime.datetime.strptime(date_time_str, '%d-%m-%Y %H:%M')
        y = row[2]
        plt.plot(x, y, marker='o')

plt.xlabel('Date and Time')
plt.ylabel('Read Value')
plt.title('Readings')
plt.show()
plt.savefig('readings.png')
plt.show()








