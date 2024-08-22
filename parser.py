from bs4 import BeautifulSoup

def parse_matches(page_content):
    soup = BeautifulSoup(page_content, 'lxml')
    matches = soup.find_all("li", class_="match-header-holder")
    all_matches = []

    for match in matches:
        span_elements = match.find_all("span")
        team1 = span_elements[0].text.strip() if len(span_elements) >= 1 else "N/A"
        team2 = span_elements[1].text.strip() if len(span_elements) >= 2 else "N/A"
        
        match_details = {
            "البطولة": match.find("h6").text if match.find("h6") else "N/A",
            "الفريق الاول": team1,
            "الفريق الثانى": team2
        }
        all_matches.append(match_details)
    
    return all_matches
