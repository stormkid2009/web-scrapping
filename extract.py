from bs4 import BeautifulSoup
import re

with open("mailBox.html", "r") as f:
    html_content = f.read()
page = BeautifulSoup(html_content, "lxml")


def extract_emails(text):
    # Define the regular expression for email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all email addresses in the text using the regular expression
    emails = re.findall(email_pattern, text)
    
    return emails


# pass the text extracted from the body element to the extract_emails function
emails = extract_emails(page.find("body").get_text(separator="\n"))
print("Extracted emails:", emails)