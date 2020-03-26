from datetime import timedelta, date

def daterange(date1, date2):
    while date1 < date2:
        yield date1, date1 + timedelta(14)
        date1 = date1 + timedelta(15)

start_dt = date(2010, 1, 1)
end_dt = date(2020, 3, 25)

