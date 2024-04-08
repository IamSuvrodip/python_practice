# Exponential Backoff //it use in password reset and it use in otp sending time

# impliment an exponetial backoff strategy that doubles that wait time betwwen retries,starting from 1 second, but stops after 5 retries.

import time

wait_time = 1
max_retries = 5
attempt = 0

while attempt < max_retries:
    print("Attempt",attempt + 1, "Wait Time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempt += 1

