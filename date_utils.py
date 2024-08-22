from datetime import datetime

def get_valid_date():
    while True:
        date_input = input("Please enter the current date using format YYYY-MM-DD: ")
        try:
            # Parse the input date, handling formats without leading zeros
            valid_date = datetime.strptime(date_input, "%Y-%m-%d")
            current_date = datetime.now().date()

            if valid_date.date() > current_date:
                print("The entered date is in the future. Please enter today's date or a past date.")
            elif valid_date.year < 1900:  # Adjust the year as needed
                print("The entered date is too far in the past. Please enter a more recent date.")
            else:
                return valid_date
        except ValueError:
            print("Invalid date format. Please try again.")
