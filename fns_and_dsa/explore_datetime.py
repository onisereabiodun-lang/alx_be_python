from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format: YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date


def calculate_future_date(current_date):
    """
    Asks the user for number of days and shows the resulting future date
    """
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    current = display_current_datetime()
    print()  # empty line for better readability
    calculate_future_date(current)