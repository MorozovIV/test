import time
t_start = time.monotonic()
time.sleep(0.0015)
time.monotonic() - t_start
print(t_start)
print(time.monotonic())