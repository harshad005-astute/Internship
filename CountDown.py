import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # overwrite the same line
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

# Take input from user
try:
    total_seconds = int(input("Enter time in seconds: "))
    countdown(total_seconds)
except ValueError:
    print("Please enter a valid number.")
