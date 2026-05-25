import time
from plyer import notification
import winsound

# interval in seconds (3600 = 1 hour, 1200 = 20 min, etc.)
while True:
    try:
        hours = float(input("After how many hours should I remind you to drink water? "))
        
        if hours <= 0:
            print("Please enter a value greater than 0.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")
INTERVAL = hours * 3600  # change this as you want

def drink_water_reminder():
    while True:
        # Notification
        notification.notify(
            title="💧 Drink Water Reminder",
            message="Stay hydrated! Drink some water now.",
            timeout=10
        )

        # Beep sound (Windows only)
        duration = 1000  # milliseconds
        frequency = 1000  # Hz
        winsound.Beep(frequency, duration)

        # Wait for next reminder
        time.sleep(INTERVAL)

if __name__ == "__main__":
    print(f"Water reminder started! You will be reminded every {hours} hour(s).")
    print("Press Ctrl+C to stop the application.")
    drink_water_reminder()