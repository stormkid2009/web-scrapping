import requests

def fetch_page(date):
    try:
        response = requests.get(f"https://www.filgoal.com/matches/?date={date}")
        response.raise_for_status()  # Raises an error for bad status codes
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page for {date}: {e}")
        return None
