import requests
from bs4 import BeautifulSoup
import csv
date = input("please enter current date using format YYYY-MM-DD:  ")
#get the page object from requests 
page =  requests.get(f"https://www.filgoal.com/matches/?date={date}") # Replace with your target URL

def main(page):
# parsing the html content
    soup = BeautifulSoup(page.content,'lxml')
# searching for the matches of the day
    matches = soup.find_all("li",class_="match-header-holder")
    all_matches = []
    match_details = {"البطولة":"","الفريق الاول":"","الفريق الثانى":""}
    for match in matches:
        span_elements = match.find_all("span")
        if(len(span_elements)>=2):
            team1=span_elements[0].text.strip()
            team2= span_elements[1].text.strip()
        else:
            team1="N/A"
            team2 = "N/A"
        match_details = {
            "البطولة": match.find("h6").text if match.find("h6") else "N/A",
            "الفريق الاول": team1,
            "الفريق الثانى": team2
        }
        all_matches.append(match_details)

    # Write to CSV file
    with open('matches.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["البطولة", "الفريق الاول", "الفريق الثانى"])
        writer.writeheader()
        writer.writerows(all_matches)

    print("Data written to matches.csv")

main(page)
