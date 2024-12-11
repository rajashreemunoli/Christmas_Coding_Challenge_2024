import time
from datetime import datetime

def countdown_to_christmas():
    # Set the date for Christmas (December 25th)
    christmas_date = datetime(2024, 12, 25, 0, 0, 0)

    # Run the countdown until Christmas
    while True:
        # Get the current time
        now = datetime.now()

        # Calculate the time difference between now and Christmas
        time_left = christmas_date - now

        # Break the countdown when Christmas is reached
        if time_left.total_seconds() <= 0:
            print("Merry Christmas! 🎄🎅")
            break

        # Extract days, hours, minutes, and seconds
        days = time_left.days
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Clear the console and print the updated countdown
        print(f"\r{days} days, {hours:02}:{minutes:02}:{seconds:02} left until Christmas🎄🎅!", end="")
        
        # Wait for 1 second before updating the countdown
        time.sleep(1)

if __name__ == "__main__":
    countdown_to_christmas()