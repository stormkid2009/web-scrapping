from date_utils import get_valid_date
from fetcher import fetch_page
from parser import parse_matches
from writer import write_to_csv
from datetime import timedelta

def main():
    start_date = get_valid_date()
    all_matches = []

    # Fetch matches for each day of the week starting from the entered date
    for i in range(7):
        current_date = start_date + timedelta(days=i)
        page = fetch_page(current_date.strftime("%Y-%m-%d"))
        if page:
            matches = parse_matches(page.content)
            for match in matches:
                match["التاريخ"] = current_date.strftime("%Y-%m-%d")
            all_matches.extend(matches)

    if all_matches:
        write_to_csv(all_matches)
    else:
        print("No match data found for the specified dates.")

if __name__ == "__main__":
    main()
