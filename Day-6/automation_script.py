import os
import time

print("Listing files every 3 seconds...")
for i in range(3):
    os.system("ls")
    time.sleep(3)
