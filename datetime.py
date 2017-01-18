from datetime import datetime
now = datetime.now() # 获取当前datetime
print(now)
print(type(now))

dt = datetime(2015, 4, 19, 12, 20)
print(dt)

print(dt.timestamp())

t = 1429417200.0
print(datetime.fromtimestamp(t))

print(datetime.utcfromtimestamp(t))

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

now = datetime.now()
print(now.strftime('%a, %b %H:%M'))

from datetime import datetime, timedelta
now = datetime.now()
print(now)
datetime(2015, 5, 18, 16, 57, 3, 540997)

print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

from datetime import datetime , timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8))
now= datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)


utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)















