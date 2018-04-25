import datetime
import pytz


# date = datetime.date(2018, 3, 20)
# print(date)

# tday = datetime.date.today()
# print(tday)
# print(tday.weekday())
# print(tday.isoweekday())

# weekday = Monday - 0 and Sunday - 6
# isoweekday = Monday - 1 and Sunday - 7


# tday = datetime.date.today()

# tdelta = datetime.timedelta(days=7)
# print(tday + tdelta)


# tday = datetime.date.today()

# bday = datetime.date(2018, 11, 25)

# till_bday = bday - tday
# print(till_bday)


# date2 = date1 + timedelta
# timedelta = date1 + date2


# time = datetime.time(12, 30, 34, 10000)
# print(time)


# dt = datetime.datetime(2018, 4, 17, 12, 30, 50, 10000)
# print(dt)


# dt = datetime.datetime(2018, 4, 17, 12, 45, 50)

# tdelta = datetime.timedelta(hours=7)
# print(dt + tdelta)


# today = datetime.datetime.today()
# now = datetime.datetime.now()
# utcnow = datetime.datetime.utcnow()

# print(today)
# print(now)
# print(utcnow)


# dt = datetime.datetime(2018, 4, 17, 11, 30, 45, tzinfo=pytz.UTC)
# print(dt)


# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)


# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)

# calc_tz = dt_utcnow.astimezone(tz=pytz.timezone('Asia/Calcutta'))
# print(calc_tz)


# calc_tz = datetime.datetime.now(tz=pytz.UTC)

# shanghai_tz = calc_tz.astimezone(tz=pytz.timezone('Asia/Shanghai'))
# print(shanghai_tz)


# calc_tz = datetime.datetime.now()
#
# mtn_tz = calc_tz.astimezone(tz=pytz.timezone('US/Mountain'))
# print(mtn_tz)


# calc_tz = datetime.datetime.now()

# paris_tz = calc_tz.astimezone(tz=pytz.timezone('Europe/Paris'))
# print(paris_tz)


# for tz in pytz.all_timezones:
#     print(tz)


dt_calc = datetime.datetime.now(tz=pytz.timezone('Asia/Calcutta'))
# print(dt_calc)

# print(dt_calc.strftime('%B %d, %Y'))


# dt_str = 'April 17, 2018'

# dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
# print(dt)


# strftime - Datetime to String
# strptime - String to Datetime
