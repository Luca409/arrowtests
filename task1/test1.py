import arrow
import datetime

start = datetime.datetime(2013, 5, 5, 12, 30)
end = datetime.datetime(2013, 5, 5, 17, 15)
for r in arrow.Arrow.span_range('hour', start, end):
	print(r)
