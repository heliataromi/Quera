from datetime import datetime, timedelta

t1 = datetime.strptime(input(), '%H:%M:%S')
t2 = datetime.strptime(input(), '%H:%M:%S')

if t2 <= t1:
    t2 += timedelta(days=1)

difference = t2 - t1

total_seconds = int(difference.total_seconds())

hours, remainder = divmod(total_seconds, 3600)
minutes, seconds = divmod(remainder, 60)

formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
print(formatted_time)