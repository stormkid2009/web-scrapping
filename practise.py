from bs4 import BeautifulSoup

# scrapping offline page with reading system file mode
with open("mailBox.html", "r") as f:
    html_content = f.read()
page = BeautifulSoup(html_content, "lxml")
print(page.title.text)