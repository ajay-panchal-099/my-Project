from datetime import datetime
import time
val1 = datetime.now()
time.sleep(1)
val2 = datetime.now()

difference = val2 - val1

print(difference.total_seconds())