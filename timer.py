import time
mytime = int(input("Enter time in seconds: "))

for i in range(mytime , 0, -1):
    seconds = i % 60
    minutes = i // 60
    print(f"{minutes:02d}:{seconds:02d}")
    time.sleep(1)

print("Time's up!")