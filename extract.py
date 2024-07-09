import re

def extract_emails(text):
    # Define the regular expression for email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all email addresses in the text using the regular expression
    emails = re.findall(email_pattern, text)
    
    return emails

# Example usage
text = """
Here are some email addresses for testing:
john.doe@example.com, jane.doe@subdomain.example.org,
info@my-site.com, support@service.io, and test@domain.co.uk
"""

emails = extract_emails(text)
print("Extracted emails:", emails)
