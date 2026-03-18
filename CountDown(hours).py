import time

def countdown(seconds):
    while seconds:
        hrs, remainder = divmod(seconds, 3600)
        mins, secs = divmod(remainder, 60)
        timer = f"{hrs:02d}:{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

total_seconds = int(input("Enter time in seconds: "))
countdown(total_seconds)
