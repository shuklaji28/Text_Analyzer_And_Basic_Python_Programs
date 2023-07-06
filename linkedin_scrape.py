# import requests
# from bs4 import BeautifulSoup

# # URL of the webpage you want to scrape
# url = "https://www.linkedin.com/in/shresthshuklaji"

# # Send a GET request to the webpage
# response = requests.get(url)

# # Create a BeautifulSoup object with the webpage content
# soup = BeautifulSoup(response.content, "html.parser")

# # Find specific elements on the page
# # Example: Find all the links on the page
# links = soup.find_all("gmail.com")

# # Extract and print the links
# for link in links:
#     href = link.get("href")
#     print(href)

"""
import requests
from bs4 import BeautifulSoup

# URL of the LinkedIn profile you want to scrape
url = "https://www.linkedin.com/in/shresthshuklaji"

# Send a GET request to the webpage
response = requests.get(url)

# Create a BeautifulSoup object with the webpage content
soup = BeautifulSoup(response.content, "html.parser")

# Find specific elements on the page
# Example: Find all the email addresses within <a> tags
email_tags = soup.find_all("a", href=lambda href: href and "mailto:" in href)

# Extract and print the email addresses
for tag in email_tags:
    email = tag["href"].split(":")[1]
    print(email)
"""

# Here's how to check if there's any gmail element in a website.

import requests
import re
from bs4 import BeautifulSoup

# URL of your LinkedIn profile
url = "https://lyne.ai/is-it-possible-to-scrape-linkedin/"

# Send a GET request to the webpage
response = requests.get(url)

# Create a BeautifulSoup object with the webpage content
soup = BeautifulSoup(response.content, "html.parser")

# Find the element containing your name
name_element = soup.find("h1", class_="entry-title")

# Extract your name
name = name_element.text.strip() if name_element else "Name not found"

# Checking for gmail content
email_elements = soup.find_all(text=lambda text: text and re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text))

emails = [email.strip() for email in email_elements] if email_elements else ["No gmail"]
for email in emails:
    print(email)
# Find the element containing your headline
headline_element = soup.find("h2", class_="mt1 t-18 t-black t-normal break-words")

# Extract your headline
headline = headline_element.text.strip() if headline_element else "Headline not found"

# Print your name and headline
print("Name:", name)
print("Headline:", headline)
