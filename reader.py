// Log in to https://www.esbnetworks.ie/ and go to the "My Account" page

import requests
from bs4 import BeautifulSoup

# Log in to the website
session_requests = requests.session()
login_url = "https://www.esbnetworks.ie/login"
result = session_requests.get(login_url)
soup = BeautifulSoup(result.text, "html.parser")
authenticity_token = soup.find("input", {"name": "authenticity_token"})["value"]
payload = {
    "authenticity_token": authenticity_token,
    "user[email]": "daniel.cregg@gmail.com",    # Replace with your email
    


